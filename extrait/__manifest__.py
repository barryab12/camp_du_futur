# -*- coding: utf-8 -*-
{
    'name': "Extrait d'acte de naissance",
    'version': '1.5.1',
    'summary': """Renseigner les informations sur les parents.""",
    'description': """
        Ce module permet d'enregistrer les infos suivantes:
        - Nom
        - Prénoms
        - Date de naissance
        - Ville de naissance
        - Profession
        - Photo
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