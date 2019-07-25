
# -*- coding: utf-8 -*-
from odoo import models, fields,api


class CandidatCandidat(models.Model):
	_name = 'model.candidat'
	_rec_name = "noter"
	
	noter = fields.Many2one('res.users',string='Selectionner')
	note = fields.Selection(string='Noter',selection=[('0', '0'), ('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('1', '12'),('13', '13'),('14', '14'),('15', '15'),('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20')])
							
    						
	@api.depends('note')
	@api.multi
	def _note(self):
		i = 0
		for rec in self:
			for x in rec.note:
				if x != '':
					i += 1
		rec.note = str(i)
	

	




	
	
	
	
