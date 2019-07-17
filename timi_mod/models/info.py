# -*- coding: utf-8 -*-

from odoo import models, fields

class PerePere(models.Model):
	_name = 'pere.pere'

	nom = fields.Char(string='Nom', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')


class MereMere(models.Model):
	_name = 'mere.mere'

	nom = fields.Char(string='Nom', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')



class ExtraitExtrait(models.Model):
	_name = 'extrait.extrait'

	nom = fields.Char(string='Nom', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date_de_naissance= fields.Date(string='date_de_naissance', required=True)
	lieu_de_naissance = fields.Char(string='lieu_de_naissance', required=True)
	nom_du_pere = fields.Many2one( comodel_name="pere.pere", string='nom_du_pere', required=True)
	nom_de_la_mere= fields.Many2one(comodel_name="mere.mere", string='nom_de_la_mere', required=True)
	numero_de_l_extrait = fields.Char(string='numero_de_l_extrait')
	heure = fields.Char(string='Heure', required=True)

