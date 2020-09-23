# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class CleanData(models.TransientModel):
    _name = 'clean.data'
    _description = 'Clean Data'

    so_do = fields.Boolean("Sales Delivery Orders", default=False)
    po = fields.Boolean('Purchase', default=False)
    all_trans = fields.Boolean('All Transfers', default=False)
    inv_pymt = fields.Boolean('Invoicing, Payments', default=False)
    journals = fields.Boolean('All Journal Entries', default=False)
    cus_ven = fields.Boolean('Customers & Vendors', default=False)
    coa = fields.Boolean('Chart Of Accounts', default=False)
    pos = fields.Boolean('Point Of Sale', default=False)
    all_data = fields.Boolean('All Data', default=False)
    mrp = fields.Boolean('Manufacturing', default=False)

    @api.multi
    def _clear_so_order(self):
        sq = "delete from stock_quant"
        sml = "delete from stock_move_line"
        sm = "delete from stock_move"
        sp = "delete from stock_picking"
        ail = "delete from account_invoice_line"
        ai = "delete from account_invoice"
        sol = "delete from sale_order_line"
        so = "delete from sale_order"
        self._cr.execute(sq)
        self._cr.execute(sml)
        self._cr.execute(sm)
        self._cr.execute(sp)
        self._cr.execute(ail)
        self._cr.execute(ai)
        self._cr.execute(sol)
        self._cr.execute(so)

    @api.multi
    def _clear_po(self):
        sq = "delete from stock_quant"
        sml = "delete from stock_move_line"
        sm = "delete from stock_move"
        sp = "delete from stock_picking"
        ail = "delete from account_invoice_line"
        ai = "delete from account_invoice"
        pol = 'delete from purchase_order_line'
        po = 'delete from purchase_order'
        self._cr.execute(sq)
        self._cr.execute(sml)
        self._cr.execute(sm)
        self._cr.execute(sp)
        self._cr.execute(ail)
        self._cr.execute(ai)
        self._cr.execute(pol)
        self._cr.execute(po)

    @api.multi
    def _clear_transfer(self):
        sq = "delete from stock_quant"
        sml = "delete from stock_move_line"
        sm = "delete from stock_move"
        sp = "delete from stock_picking"
        self._cr.execute(sq)
        self._cr.execute(sml)
        self._cr.execute(sm)
        self._cr.execute(sp)

    @api.multi
    def _clear_inv_pymt(self):
        apr = "delete from account_partial_reconcile"
        aml = "delete from account_move_line"
        am = "delete from account_move"
        ail = "delete from account_invoice_line"
        ai = "delete from account_invoice"
        ap = "delete from account_payment"
        self._cr.execute(apr)
        self._cr.execute(aml)
        self._cr.execute(am)
        self._cr.execute(ail)
        self._cr.execute(ai)
        self._cr.execute(ap)

    @api.multi
    def _clear_cus_ven(self):
        rp = "delete from res_partner where id not in " \
             "(select partner_id from res_users union select partner_id from res_company);"
        self._cr.execute(rp)

    @api.multi
    def _clear_coa(self):
        at = "delete from account_tax"
        coa = "delete from account_account"
        self._cr.execute(at)
        self._cr.execute(coa)

    @api.multi
    def _clear_journal(self):
        aml = "delete from account_move_line"
        am = "delete from account_move"
        self._cr.execute(aml)
        self._cr.execute(am)

    @api.multi
    @api.onchange('all_data')
    def all_true(self):
        for rec in self:
            if rec.all_data:
                rec.so_do = True
                rec.po = True
                rec.all_trans = True
                rec.inv_pymt = True
                rec.journals = True
                rec.cus_ven = True
                rec.coa = True
            else:
                rec.so_do = False
                rec.po = False
                rec.all_trans = False
                rec.inv_pymt = False
                rec.journals = False
                rec.cus_ven = False
                rec.coa = False

    @api.multi
    def clean_data(self):
        for rec in self:
            if rec.all_data:
                self._clear_so_order()
                self._clear_po()
                self._clear_transfer()
                self._clear_inv_pymt()
                self._clear_cus_ven()
                self._clear_coa()
                self._clear_journal()
            if rec.so_do:
                self._clear_so_order()
            if rec.po:
                self._clear_po()
            if rec.all_trans:
                self._clear_transfer()
            if rec.inv_pymt:
                self._clear_inv_pymt()
            if rec.journals:
                self._clear_journal()
            if rec.cus_ven:
                self._clear_cus_ven()
            if rec.coa:
                self._clear_coa()