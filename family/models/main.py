# -*- coding: utf-8 -*-

from odoo import models, fields

class PerePere(models.Model):
	_name = 'mod.pere'
	nom = fields.Char(string='Nom', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')


class MereMere(models.Model):
	_name = 'mod.mere'
	nom = fields.Char(string='Nom', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')