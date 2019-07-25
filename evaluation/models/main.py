# -*- coding: utf-8 -*-

from odoo import models, fields,api


class EvalCandidat(models.Model):
	_name = 'mod.candidat'
	_rec_name = ("cdt")
	
	cdt = fields.Many2one('res.users', string='Candidats')
	nom = fields.Many2one('res.users', string='Noté par')
	note = fields.Char(string='Note', placeholder='Notez le candidat')
	