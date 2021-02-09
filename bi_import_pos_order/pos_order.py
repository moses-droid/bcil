# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import time
import datetime
import tempfile
import binascii
import xlrd
import io
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from datetime import date, datetime
from odoo.exceptions import Warning
from odoo import models, fields, exceptions, api, _
import logging
_logger = logging.getLogger(__name__)

try:
    import csv
except ImportError:
    _logger.debug('Cannot `import csv`.')
try:
    import cStringIO
except ImportError:
    _logger.debug('Cannot `import cStringIO`.')
try:
    import base64
except ImportError:
    _logger.debug('Cannot `import base64`.')



class pos_order(models.Model):
    _inherit = "pos.order"

    custom_name = fields.Char(string="Name")


class gen_pos_order(models.TransientModel):
    _name = "gen.pos.order"

    file_to_upload = fields.Binary('File')
    import_option = fields.Selection([('csv', 'CSV File'),('xls', 'XLS File')],string='Select',default='csv')

    @api.multi
    def find_session_id(self, session ):    
        if session:
            session_ids  = self.env['pos.session'].search([('name', '=', session )])
        if session_ids:
            session_id = session_ids[0]                     
            return session_id
        else:
            raise Warning(_('Wrong Session %s') % session)

    @api.multi
    def find_partner(self, partner_name):
        partner_ids = self.env['res.partner'].search([('name', '=', partner_name)])
        if len(partner_ids) != 0:
            partner_id  = partner_ids[0]
            return partner_id
        else:
            raise Warning(_('Wrong Partner %s') % partner_name)

    @api.multi
    def check_product(self, product):   
        product_ids = self.env['product.product'].search([('name', '=', product)])
        if product_ids:
            product_id  = product_ids[0]
            return product_id
        else:
            raise Warning(_('Wrong Product %s') % product)

    @api.multi
    def find_sales_person(self, name):
        sals_person_obj = self.env['res.users']
        partner_search = sals_person_obj.search([('name', '=', name)])
        if partner_search:
            return partner_search
        else:
            raise Warning(_('Not Valid Salesperson Name "%s"') % name)

    @api.multi
    def make_pos(self, values):
        pos_obj = self.env['pos.order']
        partner_id = self.find_partner(values.get('partner_id'))
        salesperson_id = self.find_sales_person(values.get('salesperson'))
        session_id  = self.find_session_id(values.get('session'))             
        if partner_id and salesperson_id and session_id:
            pos_search = pos_obj.search([('partner_id','=',partner_id.id),('session_id','=',session_id.id),('user_id','=',salesperson_id.id),('custom_name','=',values.get('name'))])
            if pos_search:
                pos_search = pos_search[0]
                pos_id  = pos_search
            else:
                pos_id = pos_obj.create({
                                        'custom_name' : values.get('name'),
                                        'partner_id' : partner_id.id or False,
                                        'user_id':salesperson_id.id or False,
                                        'session_id':session_id.id or False,
                                        'date_order':values.get('date_order'),
                                        'import_pos_order':True,
                                        'amount_paid' : 0.0,
                                        'amount_return' : 0.0,
                                        'amount_tax' : 0.0,
                                        'amount_total' : 0.0,
                                        })
            line = self.make_pos_line(values, pos_id)
            currency = pos_id.pricelist_id.currency_id
            pos_id.amount_paid = sum(payment.amount for payment in pos_id.statement_ids)
            pos_id.amount_return = sum(payment.amount < 0 and payment.amount or 0 for payment in pos_id.statement_ids)
            pos_id.amount_tax = currency.round(sum(pos_id._amount_line_tax(line, pos_id.fiscal_position_id) for line in pos_id.lines))
            amount_untaxed = currency.round(sum(line.price_subtotal for line in pos_id.lines))
            pos_id.amount_total = pos_id.amount_tax + amount_untaxed
        return pos_id
            
    @api.multi
    def make_pos_line(self, values,pos_id):
        pos_line_obj = self.env['pos.order.line']
        pos_obj = self.env['pos.order']

        if values.get('product_id'):
            product_name = values.get('product_id')  
            if self.check_product(product_name) != None:
                product_id = self.check_product(product_name)

            if values.get('quantity'):
                quantity = values.get('quantity')  

            if values.get('price_unit'):
                price_unit = values.get('price_unit')  

            if values.get('discount'):
                discount = values.get('discount') 

            tax_ids  = []
            if values.get('tax') : 

                
                if ';' in  values.get('tax'):
                    tax_names = values.get('tax').split(';')
                    for name in tax_names:
                        tax= self.env['account.tax'].search([('name', '=', name),('type_tax_use','=','sale')])
                        if not tax:
                            raise Warning(_('"%s" Tax not in your system') % name)
                        tax_ids.append(tax.id)

                elif ',' in  values.get('tax'):
                    tax_names = values.get('tax').split(',')
                    for name in tax_names:
                        tax= self.env['account.tax'].search([('name', '=', name),('type_tax_use','=','sale')])
                        if not tax:
                            raise Warning(_('"%s" Tax not in your system') % name)
                        tax_ids.append(tax.id)
                else:
                    tax_names = values.get('tax').split(',')
                    tax= self.env['account.tax'].search([('name', '=', tax_names),('type_tax_use','=','sale')])
                    if not tax:
                        raise Warning(_('"%s" Tax not in your system') % tax_names)
                    tax_ids.append(tax.id)


            line = pos_line_obj.create({
                                'product_id': product_id.id ,
                                'qty': quantity,
                                'price_unit': price_unit,
                                'discount': discount ,
                                'order_id': pos_id.id,
                                'price_subtotal' : 0.0,
                                'price_subtotal_incl' : 0.0,
                                })

            if tax_ids:
                line.write({'tax_ids':([(6,0,tax_ids)])}) 
            line._onchange_amount_line_all() 
        return values
        
    @api.multi
    def import_pos_order(self):
        if  self.import_option == 'csv':
                keys = ['name','session','date_order','salesperson','partner_id','product_id','quantity','price_unit','discount','tax']
                csv_data = base64.b64decode(self.file_to_upload)
                data_file = io.StringIO(csv_data.decode("utf-8"))
                data_file.seek(0),
                file_reader = []
                csv_reader = csv.reader(data_file, delimiter=',')
                try:
                    file_reader.extend(csv_reader)
                except Exception:
                    raise exceptions.Warning(_("Invalid file!"))
                values = {}
                lines = []  
                for i in range(len(file_reader)):
                    field = map(str, file_reader[i])
                    values = dict(zip(keys, field))
                    if values:
                        if i == 0:
                            continue
                        else:
                            res = self.make_pos(values)
        else:
            fp = tempfile.NamedTemporaryFile(delete = False, suffix=".xlsx")
            fp.write(binascii.a2b_base64(self.file_to_upload))
            fp.seek(0)
            values = {}
            workbook = xlrd.open_workbook(fp.name)
            sheet = workbook.sheet_by_index(0)
            lines = []
            for row_no in range(sheet.nrows):
                val = {}
                if row_no <= 0:
                    fields = map(lambda row:row.value.encode('utf-8'), sheet.row(row_no))
                else:
                    line = list(map(lambda row:isinstance(row.value, bytes) and row.value.encode('utf-8') or str(row.value), sheet.row(row_no)))
                    values =  {     
                                'name':line[0],
                                'session': line[1],
                                'date_order': line[2],
                                'salesperson': line[3],
                                'partner_id': line[4],
                                'product_id': line[5],
                                'quantity': line[6],
                                'price_unit': line[7],
                                'discount': line[8],
                                'tax' : line[9]
                              }
                    res = self.make_pos(values)



