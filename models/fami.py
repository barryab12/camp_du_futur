

# -*- coding : utf-8 -*-

from odoo import models, fields

class PerePere(models.Model):
    
    _name = 'pere.pere'
  

    nom = fields.Char(string= "Nom",required = True) 

    Prenom = fields.Char(string= "Prenom",required = True) 

    date = fields.Date(string= "Date_de_naissance") 

    ville = fields.Char(string= "Ville_de_naissance")

    profession = fields.Char(string= "Profession",required = True) 

    photo = fields.Binary(string= "photo") 

class MereMere(models.Model):
    
    _name = 'mere.mere'
  

    nom = fields.Char(string= "Nom",required = True) 

    Prenom = fields.Char(string= "Prenom",required = True) 

    date = fields.Date(string= "Date_de_naissance") 

    ville = fields.Char(string= "Ville_de_naissance")

    profession = fields.Char(string= "Profession",required = True) 

    photo = fields.Binary(string= "photo") 