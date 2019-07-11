from odoo import models, fields, api

class NouveauModele(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    sal = fields.Integer(string="Votre salaire", required=True)

    multi = fields.Selection(string="Multiplier",selection=[('DOUBLE','Doubler'),('TRIPLE','Tripler')])

    nv_sal = fields.Integer(string="Nouveau salaire", compute="_compute_nv_sal", store=True)

    @api.depends('sal', 'multi')
    def _compute_nv_sal(self):
    	for record in self:
    		if record.multi == 'DOUBLE':
    			record.nv_sal = record.sal * 2

    		elif record.multi == 'TRIPLE':
    			record.nv_sal = record.sal * 3

    		else:
    			record.nv_sal = record.sal