# -*- coding: utf-8 -*-

from odoo import models, fields,api
from random import randint

class PerePere(models.Model):
	_name = 'pere.pere'

	nom = fields.Char(string='Nom', required=True)
	prenom = fields.Char(string='Prenom')
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')
	matricule = fields.Char(string='Matricule', compute='_matricule', readonly=True, store=True)
	enfants = fields.One2many('extrait.extrait',inverse_name='nom_du_pere',string='Enfants')
	


	@api.depends('nom')
	def _matricule(self):
		for rec in self:
			a = rec.nom[:3]
			s = ''
			while len(s) < 5:
				c = randint(0,9)
				s += str(c)
			rec.matricule = a.upper() + s


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
	prenom = fields.Char(string='Prenom')
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')
	matricule = fields.Char(string='Matricule', compute='_matricule', readonly=True, store=True)
	enfants = fields.One2many('extrait.extrait',inverse_name='nom_de_la_mere',string='enfants')


	@api.depends('nom')
	def _matricule(self):
		for rec in self:
			a = rec.nom[:3]
			s = ''
			while len(s) < 5:
				c = randint(0,9)
				s += str(c)
			rec.matricule = a.upper() + s


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
	prenom = fields.Char(string='Prenom')
	date_de_naissance= fields.Date(string='date_de_naissance')
	lieu_de_naissance = fields.Char(string='lieu_de_naissance')
	nom_du_pere = fields.Many2one( comodel_name="pere.pere", string='nom_du_pere')
	nom_de_la_mere= fields.Many2one(comodel_name="mere.mere", string='nom_de_la_mere')
	matricule = fields.Char(string='Matricule', compute='_matricule', readonly=True, store=True)

	@api.depends('nom')
	def _matricule(self):
		for rec in self:
			
			a = rec.nom_du_pere.nom[:2]
			b = rec.nom_de_la_mere.nom[:2]
			c = a + b
			s = ''
			while len(s) < 5:
				d = randint(0,9)
				s += str(d)
			rec.matricule = c.upper() + s


	
	@api.multi
	def name_get(self):
		result = []
		for extraitextrait in self:
			name = extraitextrait.nom + ' ' + extraitextrait.prenom
			result.append((extraitextrait.id, name))
		return result
			

