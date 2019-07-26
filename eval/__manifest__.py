# -*- coding: utf-8 -*-
{
    'name': "Eval",

    'summary': """Ce module permet au candidat d'avoir une note""",

    'description': """
        Ce module permet :
        - A un étudiant de deposer son devoir ou sa compo
        - A attribuer des notes à d'autres étudiants
        - D'obtenir une note
    """,

    'author': "Joshua Guei",
    'website': "http://www.groupecerco.com",

    'version': '0.1',

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'application':True,
    'auto_install':False,
}
