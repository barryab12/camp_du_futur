# -*- coding: utf-8 -*-
{
    'name': "Extrait d'acte de naissance",
    'version': '2.7.1',
    'summary': """Créer un extrait d'acte de naissance format PDF""",
    'description': """
        Ce module permet de créer et gérer la confection d'acte
        de naissance.
    """,
    'author': "Kevin Pierre",
    'maintainer': "Kevin Pierre",
    'category': "Registre",
    'company': "Cerco Dev",
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'application':True,
    'auto_install':False,
    'depends': ['base'],
    'data':[
            "views/vue.xml",
            "views/extrait_vue.xml",
            "security/ir.model.access.csv"
            ],
    'website': "http://www.groupecerco.com"
}