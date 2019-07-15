# -*- coding: utf-8 -*-

from odoo import models, fields

class pere(models.Model):
	_name = 'en.pere'

	nom = fields.Char(string="Nom", required=True)
	prenom = fields.Char(string="Prenom", required=True)
	d_naissance = fields.Date(string="Date de naissance", required=True)
	ville_n = fields.Char(string="Entrez votre ville de naissance")
	prof = fields.Char(string="Profession")
	photo = fields.Binary(string='Image')


class mere(models.Model):
	_name = 'en.mere'

	nom = fields.Char(string="Nom", required=True)
	prenom = fields.Char(string="Prenom", required=True)
	d_naissance = fields.Date(string="Date de naissance", required=True)
	ville_n = fields.Char(string="Entrez votre ville de naissance")
	prof = fields.Char(string="Profession")
	photo = fields.Binary(string='Image')