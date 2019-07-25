# -*- coding: utf-8 -*-

{
    'name': "Evaluation",
    'version': '0.2.1',
    'summary': """Gerez les travaux des candidats""",
    'description': """
        Module qui permet à 5 candidats de
        noter 1 autre et vice-versa
    """,
    'author': "Kevin Pierre",
    'maintainer': "Kevin Pierre",
    'category': "Evaluations",
    'company': "Cerco Dev",
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'application':True,
    'auto_install':False,
    'depends': ['base'],
    'data':[
            "views/vue.xml",
            "security/ir.model.access.csv"
            ],
    'website': "http://www.groupecerco.com"
}
