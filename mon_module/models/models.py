# -*- coding: utf-8 -*-

from odoo import models, fields

class ExtraitPere(models.Model):
    _name = 'mod.pere'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")

# class ExtraitMere(models.Model):
#     _name = 'mod.mere'

#     nom = fields.Char(string="Nom", required=True)
#     prenom = fields.Char(string="Prénoms", required=True)
#     dn = fields.Date(string="Date de naissance")
#     ville_n = fields.Char(string="Ville de naissance")
#     prof = fields.Char(string="Profession")
#     photo = fields.Binary(string="Photo")