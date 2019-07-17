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
	pere = fields.Many2one(comodel_name='pere.pere', string="Père")
	mere = fields.Many2one(comodel_name='mere.mere', string="Mère")
	nom = fields.Char(string="""Nom de l'Enfant""", required=True)
	prenom = fields.Char(string="""Prénoms de l'Enfant""", required=True)
	date = fields.Date(string='Date de naissance', required=True)
	ville = fields.Char(string='Ville de naissance', required=True)
