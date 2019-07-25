# -*- coding: utf-8 -*-
{
    'name': "Gestion Devoir",

    'summary': """Module de gestion de devoirs""",

    'description': """Ce module permettra à un étudiant de déposer son devoir et de corriger d'autres devoirs""",

    'author': "Brou Cédrick ATSE",
    'website': "http://www.groupecerco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vue_pere.xml',
        # 'views/extrait_pdf.xml',
    ],
    # only loaded in demonstration mode
    'images': ['/Extrait/static/src/img/icon.jpeg'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}