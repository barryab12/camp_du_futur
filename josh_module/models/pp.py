# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from random import *

class PerePere(models.Model):
	_name = 'pere.pere'

	nom = fields.Char(string='Nom', required=True, default="")
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')
	matricule = fields.Char(string ="Matricule", compute ='_matricule',readonly = True, store=True)
	enfant = fields.One2many(comodel_name ='extrait.extrait', inverse_name='pere')

	@api.depends('nom','matricule')
	def _matricule(self):
		for record in self:
			record.matricule = record.nom[:3].upper() + str(randrange(99999))


	@api.multi
	def name_get(self):
		result = []
		for perepere in self:
			name = perepere.nom +' '+ perepere.prenom
			result.append((perepere.id, name))
		return result




class MereMere(models.Model):
	_name = 'mere.mere'

	nom = fields.Char(string='Nom', required=True, default="")
	prenom = fields.Char(string='Prénoms', required=True)
	date = fields.Date(string='Date de naissance')
	ville = fields.Char(string='Ville de naissance')
	profession = fields.Char(string='Profession')
	photo = fields.Binary(string='photo')
	matricule = fields.Char(string ="Matricule", compute ='_matricule',readonly = True, store=True)
	enfant = fields.One2many(comodel_name ='extrait.extrait', inverse_name='mere')

	@api.depends('nom','matricule')
	def _matricule(self):
		for record in self:
			record.matricule = record.nom[:3].upper() + str(randrange(99999))



	@api.multi
	def name_get(self):
		result = []
		for meremere in self:
			name = meremere.nom +' '+ meremere.prenom
			result.append((meremere.id, name))
		return result

class ExtraitExtrait(models.Model):
	_name = 'extrait.extrait'
	pere = fields.Many2one(comodel_name='pere.pere', string="Père", required=True, default="")
	mere = fields.Many2one(comodel_name='mere.mere', string="Mère", required=True, default="")
	nom = fields.Char(string="""Nom de l'Enfant""", required=True, default="")
	prenom = fields.Char(string="""Prénoms de l'Enfant""", required=True)
	date = fields.Date(string='Date de naissance', required=True)
	ville = fields.Char(string='Ville de naissance', required=True)
	matricule = fields.Char(string ="Matricule", compute ='_matricule',readonly = True, store=True)

	@api.depends('nom','matricule')
	def _matricule(self):
		for record in self:
			record.matricule = record.pere.nom[:2].upper() + record.mere.nom[:2].upper() + str(randrange(99999))


	@api.multi
	def name_get(self):
		result = []
		for extraitextrait in self:
			name = extraitextrait.nom +' '+ extraitextrait.prenom
			result.append((extraitextrait.id, name))
		return result
