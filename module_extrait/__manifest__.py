# -*- coding: utf-8 -*-
{
    'name': "Extrait d'acte de naissance",
    'version': '1.0.0',
    'summary': """Création d'un extrait d'acte de naissance""",
    'description': """
        CRéation d'extrait d'acte de naissance
    """,
    'author': "Jo Mederic",
    'maintainer': "Jo Mederic",
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