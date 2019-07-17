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

class Extrait(models.Model):
	_name = 'mod.extrait'

	centre = fields.Char(string='Centre de', required=True)
	date = fields.Char(string='Date de naissance', required=True)
	heure = fields.Char(string='Heure de naissance', required=True)
	noms = fields.Char(string='Nom et prénoms', required=True)
	genre = fields.Selection([('Fils','Fils'),('Fille','Fille')], required=True)
	lieu = fields.Char(string='Lieu de naissance', required=True)
	pere = fields.Many2one('mod.pere', string='Père', required=True)
	mere = fields.Many2one('mod.mere', string='Mère', required=True)
	fait = fields.Date(string='Fait le', default=fields.Date.today, required=True)
