# -*- coding: utf-8 -*-
{
    'name': "Extrait de naissance",

    'summary': """Module de création d'extrait de naissance""",

    'description': """Ce module permettra de créer des extraits de naissance""",

    'author': "Coulibaly Yelli Myriam",
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
        'views/extrait_pdf.xml',
    ],
    # only loaded in demonstration mode
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}