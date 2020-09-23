# -*- coding: utf-8 -*-
{
    'name': "Mass Clean Data (Clear Data)",
    'summary': 'This module allows user to clean records from object using wizard',
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'category': 'Tools',
    'version': '12.0.0.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'stock', 'account', 'purchase'],

    # always loaded
    'data': [
        'wizards/clean_data_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
