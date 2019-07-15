# -*- coding: utf-8 -*-
{
    'name': "Extrait d'Acte de Naissance",
    'version': '1.0.0.0',
    'summary': """information sur le père et la mère""",
    'description': """
        Ce module permet d'enregistrer les infos suivantes:
        - Nom
        - Prénoms
        - date de naissance
        - ville de naissance
        - profession
        - photo
    """,
    'author': "judith tape",
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'application':True,
    'auto_install':False,
    'depends': ['base'],
    'data':["views/vue.xml","security/ir.model.access.csv"],
    'website': "http://www.groupecerco.com"
}
