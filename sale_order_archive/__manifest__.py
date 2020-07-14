# -*- coding: utf-8 -*-
{
    'name': "Sale Order Archive",

    'summary': "Create archive object for all orders",

    'description': "Create archive object for all orders older than 7 days and delete sale.order object",

    'author': "KatBotkowska",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_archive.xml',
        'views/sale_order_archive_menu.xml',
        'data/sale_order_archive_cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto-install': False,
}
