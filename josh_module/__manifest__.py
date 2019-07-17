# -*- coding: utf-8 -*-
{
    'name': "Extrait d'Acte de Naissance",
    'version': '1.0.0.0',
    'summary': """Ce module vous permet d'imprimer un extrait de naissance""",
    'description': """
        Ce module permet d'enregistrer les infos suivantes:
        - un menu père
        - un menu mère
        - un menu extrait
    """,
    'author': "Joshua Guei",
    'images':[],
    'license':'AGPL-3',
    'installable':True,
    'application':True,
    'auto_install':False,
    'depends': ['base'],
    'data':["views/vue.xml","security/ir.model.access.csv","views/extrait_pdf.xml"],
    'website': "http://www.groupecerco.com"
}
