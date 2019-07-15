

# -*- coding: utf-8 -*-
{
    'name': "naissance",
    'version': '1.0.0.0',
    'summary': """information sur le père et la mère""",
    'description': """
        Ce module permet d'enregistrer les infos suivantes:
        - Nom
        - Prenom
        - date de naissance
        - ville de naissance
        - profession
        - photo
    """,
    'author': "myriam" ,
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'application':True,
    'auto_install':False,
    'depends': ['base'],
    'data':["views/vue.xml","security/ir.model.access.csv"],
    'website': "http://www.groupecerco.com"
}
