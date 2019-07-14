# -*- coding: utf-8 -*-
{
    'name': "Extrait d'acte de naissance",
    'version': '0.9.5',
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
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'application':True,
    'auto_install':False,
    'depends': ['base'],
    'data':["views/vue.xml","security/ir.model.access.csv"],
    'website': "http://www.groupecerco.com"
}
