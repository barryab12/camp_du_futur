# -*- coding: utf-8 -*-

from odoo import models, fields,api
from random import *

class PerePere(models.Model):
	_name = 'pere.pere'

	nom = fields.Char(string='Nom', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')
	matricule = fields.Char(string='Matricule', compute='_mati', readonly=True, store=True)
	child_ids = fields.One2many(string='child', comodel_name='extrait.extrait', inverse_name='nom_du_pere')

	@api.depends('nom')
	def _mati(self):
		for rec in self:
			lee = rec.nom[:3]
			s = ''
			while len(s) < 5:
				mit = randint(0,9)
				s += str(mit)
			rec.matricule = lee.upper() + s


	@api.multi
	def name_get(self):
		result = []
		for perepere in self:
			name = perepere.nom + ' ' + perepere.prenom
			result.append((perepere.id, name))
		return result


class MereMere(models.Model):
	_name = 'mere.mere'

	nom = fields.Char(string='Nom', required=True)
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')
	matricule = fields.Char(string='Matricule', compute='_mati', readonly=True, store=True)
	child_ids = fields.One2many(string='child', comodel_name='extrait.extrait', inverse_name='nom_de_la_mere')

	@api.depends('nom')
	def _mati(self):
		for rec in self:
			lee = rec.nom[:3]
			s = ''
			while len(s) < 5:
				mit = randint(0,9)
				s += str(mit)
			rec.matricule = lee.upper() + s


	@api.multi
	def name_get(self):
		result = []
		for meremere in self:
			name = meremere.nom + ' ' + meremere.prenom
			result.append((meremere.id, name))
		return result



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
	matricule = fields.Char(string='Matricule', compute='_mati', readonly=True, store=True)
	telecharger = fields.Many2many("ir.attachment", "partner_id", string='Telecharger')

	@api.depends('nom')
	def _mati(self):
		for rec in self:
			
			lee = rec.nom_du_pere.nom[:2]
			laa = rec.nom_de_la_mere.nom[:2]
			les = lee + laa
			s = ''
			while len(s) < 5:
				mit = randint(0,9)
				s += str(mit)
			rec.matricule = les.upper() + s
			

