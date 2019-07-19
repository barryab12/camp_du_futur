# -*- coding: utf-8 -*-
{
    'name': "Extrait de naissance",

    'summary': """Module de création d'extrait de naissance""",

    'description': """Ce module permettra de créer des extraits de naissance""",

    'author': "JUDITH tape",
    'website': "http://www.groupecerco.com",

    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/vue_pere.xml',
        'views/extrait_pdf.xml',
    ],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}