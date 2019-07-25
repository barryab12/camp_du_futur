# -*- coding: utf-8 -*-
from odoo import models, fields,api


class EvaluationEvaluation(models.Model):
	_name = 'evaluation.evaluation'
	_rec_name = ("noter")
	
	noter = fields.Many2one('res.users',string='Selectionner')
	note = fields.Selection(string=u'Note',selection=[('0', '0'), ('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')])
	identité = fields.Char(string='vous etes notez')						
    						
	@api.depends('note')
	@api.multi
	def _note(self):
		i = 0
		for rec in self:
			for x in rec.note:
				if x != '':
					i += 1
		rec.note = str(i) + " /5"
	

	




	
	
	
	
