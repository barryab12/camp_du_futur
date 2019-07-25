
# -*- coding: utf-8 -*-
from odoo import models, fields, api
 
class Notation(models.Model):
    _name = 'model.notation'
    _rec_name = 'candidat'

    candidat  = fields.Many2one(commodel_name="res.users", string="candidat" , domain=[('model.notation','in',[5])])
    note = fields.Selection(string='Note',selection=[('0', '0'), ('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')])
							
    						
	@api.onchange('note')
	@api.multi
	def _note(self):
		i = 0
		for rec in self:
			for x in rec.note:
				if x != '':
					i += 1
		rec.note = str(i)