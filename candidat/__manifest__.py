# -*- coding: utf-8 -*-
{
    'name': "Candidat",

    'summary': """Module d'inter notation""",

    'description': """Ce module permettra à des candidats de se noter les uns les autres""",

    'author': "Brou Cédrick ATSE",
    'website': "http://www.groupecerco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Candidats',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/candidat.xml',
        # 'views/extrait_pdf.xml',
    ],
    # only loaded in demonstration mode
}