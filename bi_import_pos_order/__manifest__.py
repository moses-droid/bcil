# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Import POS Orders from Excel/CSV File in odoo',
    'version': '12.0.0.4',
    'category': 'Extra tools',
    'summary': 'Easy to Import multiple pos orders order with multiple pos order lines on Odoo by Using CSV/XLS file',
    'description': """

    Import stock with Serial number import
    Import stock with lot number import
    import lot number with stock import
    import serial number with stock import
    import lines import
    import order lines import
    import orders lines import
    import so lines import
    imporr po lines import

This modules helps to pos order transaction using CSV or Excel file
    Easy to Import multiple pos orders order with multiple pos order lines on Odoo by Using CSV/XLS file
    	BrowseInfo developed a new odoo/OpenERP module apps.
	This module use for import bulk pos order from Excel file. Import pos order lines from CSV or Excel file.
	Import pos order, Import pos order line, Import pos, Import point of sale data. POS Import, Add POS from Excel.Add Excel POS order.Add CSV file.Import POS data. Import excel file

	This module use for import bulk point of sale order from Excel file. Import point of sale order lines from CSV or Excel file. Import point of sales Orders
	Import point of sale order, Import point of sale order line, Import point of sale, Import point of sales data. point of sale Import, Add point of sale from Excel.Add Excel point of sales order.Add CSV file.Import point of sales data. Import excel file

Fácil de importar pedidos de múltiples pedidos con múltiples líneas de pedido en Odoo utilizando el archivo CSV / XLS
     BrowseInfo desarrolló una nueva aplicación de módulo odoo / OpenERP.
Este módulo se usa para importar orden de pedido a granel desde el archivo de Excel. Importar líneas de pedido de pos de archivo CSV o Excel.
Importar orden de la posición, Importar línea de pedido, Importar pos, Importar datos de punto de venta. Importar punto de venta, Agregar punto de venta desde Excel. Agregar orden de punto de venta de Excel. Agregar archivo CSV. Importar datos de punto de venta. Importar archivo de Excel

Este módulo se utiliza para importar pedidos de punto de venta a granel desde el archivo de Excel. Importe las líneas de orden de punto de venta desde el archivo CSV o Excel.
Importe el pedido del punto de venta, línea de orden de punto de venta de importación, punto de venta de importación, datos de punto de venta de importación. punto de venta Importación, agregue punto de venta desde Excel.Agregue el punto de venta de Excel. Agregue el archivo CSV. Importe los datos del punto de venta. Importar archivo de Excel

من السهل استيراد متعددة أوامر ترتيب نقاط البيع مع عدة خطوط ترتيب نقاط البيع على Odoo باستخدام ملف CSV / XLS
     وضعت BrowseInfo تطبيقات الوحدة الجديدة Openoo / OpenERP.
هذه الوحدة تستخدم لاستيراد طلبية السائبة من ملف Excel. استيراد خطوط ترتيب نقاط البيع من ملف CSV أو Excel.
استيراد طلبية ، واستيراد خط الأمر ، استيراد نقاط البيع ، استيراد بيانات نقطة البيع. POS Import، Add POS from Excel.Add Excel POS order.Add CSV file.Import POS data. استيراد ملف اكسل

تستخدم هذه الوحدة لاستيراد ترتيب نقاط البيع بالجملة من ملف Excel. استيراد خطوط ترتيب نقاط البيع من ملف CSV أو Excel.
استيراد نقطة بيع النظام ، واستيراد نقطة طلب بيع خط ، نقطة استيراد بيع ، استيراد بيانات نقطة البيع. نقطة بيع استيراد ، إضافة نقطة بيع من Excel.Add نقطة Excel من المبيعات order.Add CSV file.Import نقطة بيانات المبيعات. استيراد ملف اكسل

Facile à importer plusieurs commandes de commandes POS avec plusieurs lignes de commande POS sur Odoo en utilisant le fichier CSV / XLS
     BrowseInfo a développé une nouvelle application de module odoo / OpenERP.
Ce module est utilisé pour l'importation de commandes groupées à partir du fichier Excel. Importer des lignes de commandes POS depuis un fichier CSV ou Excel.
Importer l'ordre de pos, Importer la ligne de commande de position, Importer la position, Importer le point de vente de données. POS Import, Ajouter POS à partir d'Excel.Add Excel POS order.Add CSV file.Import données POS. Importer un fichier Excel

Ce module est utilisé pour l'importation de commande de point de vente en vrac à partir du fichier Excel. Importer des lignes de commande point de vente à partir de fichier CSV ou Excel.
Commande de point de vente d'importation, ligne de commande de point de vente d'importation, point de vente d'importation, données de point de vente d'importation. point de vente Importer, Ajouter un point de vente à partir de Excel.Ajouter le point de vente Excel.Ajouter le fichier CSV.Importer les données du point de vente. Importer un fichier Excel

Fácil de importar múltiplas ordens de pedidos de postagem com múltiplas linhas de pedidos posteriores em Odoo usando o arquivo CSV / XLS
     BrowseInfo desenvolveu um novo aplicativo odoo / OpenERP.
Este módulo usa para importar encomendas em massa a partir do arquivo do Excel. Importar linhas de ordem pós do arquivo CSV ou Excel.
Importar pedido, Importar linha de pedidos, Importar, Importar os dados do ponto de venda. Importação de POS, Adicionar POS a partir do Excel. Adicionar o pedido do Excel POS. Adicionar o arquivo CSV. Importe os dados do POS. Importar arquivo excel

Este módulo usa para importar ponto de venda em massa do arquivo do Excel. Importar linhas de pedidos de ponto de venda a partir do arquivo CSV ou Excel.
Ordem de importação do ponto de venda, Importar linha de pedido de ponto de venda, Importar ponto de venda, Importar os dados do ponto de venda. Importação de ponto de venda, Adicionar ponto de venda do Excel.Adicionar a ordem do ponto de venda do Excel. Adicionar arquivo CSV. Dados do ponto de venda do mercado. Importar arquivo excel
    """,
    'author': 'BrowseInfo',
    'website': 'www.browseinfo.in',
    "price": 22,
    "currency": 'EUR',
    'depends': ['base','sale_management','point_of_sale',],
    'data': ["pos.xml"
            ],
    'qweb': [],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/LfFA_bYbCqs',
    "images":['static/description/Banner.png']
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
