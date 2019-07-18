# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import *

class PerePere(models.Model):
	_name = 'mod.pere'

	nom = fields.Char(string='Nom', default='', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')
	matricule = fields.Char(string='Matricule', compute='_matr', readonly=True, store=True)

	@api.depends('nom')
	def _matr(self):
		self.matricule = self.nom[:3].upper() + str(randrange(99999))

	@api.multi
	def name_get(self):
		res = []
		for modpere in self:
			name = modpere.nom +' '+modpere.prenom
			res.append((modpere.id, name))
		return res


class MereMere(models.Model):
	_name = 'mod.mere'

	nom = fields.Char(string='Nom', default='', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')
	matricule = fields.Char(string='Matricule', compute='_matr', readonly=True, store=True)

	@api.depends('nom')
	def _matr(self):
		self.matricule = self.nom[:3].upper() + str(randrange(99999))

	@api.multi
	def name_get(self):
		res = []
		for modmere in self:
			name = modmere.nom +' '+modmere.prenom
			res.append((modmere.id, name))
		return res

class Extrait(models.Model):
	_name = 'mod.extrait'
	_rec_name = 'noms'

	centre = fields.Char(string='Centre de', required=True)
	date = fields.Char(string='Date de naissance', required=True)
	heure = fields.Char(string='Heure de naissance', required=True)
	noms = fields.Char(string='Nom et prénoms', required=True)
	genre = fields.Selection([('FILS','Fils'),('FILLE','Fille')], required=True)
	lieu = fields.Char(string='Lieu de naissance', required=True)
	pere = fields.Many2one('mod.pere', string='Père', required=True)
	mere = fields.Many2one('mod.mere', string='Mère', required=True)
	fait = fields.Date(string='Fait le', default=fields.Date.today, required=True)
	matricule = fields.Char(string='Matricule', compute='_matr', readonly=True, store=True)

	@api.depends('nom','matricule')
	def _matr(self):
		for rec in self:
			rec.matricule = rec.pere.nom[:2].upper() + rec.mere.nom[:2].upper() + str(randrange(99999))
