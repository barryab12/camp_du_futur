from odoo import models, fields, api

class NouveauModele(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'
 
    commentaire = fields.Char(string="votre commentaire", required=True)

    selection = fields.Selection(string="selection", selection=[('OUI','oui'),('NON','non')])

    many = fields.Many2one(comodel_name="fleet.vehicle.model", string="vehicle")

    salaire = fields.Integer(string="votre salaire", required=True)

    multiplier = fields.Selection(string="multiplier", selection=[('DOUBLE','double'),('TRIPLE','triple')])

    n_salaire = fields.Integer(string="new salaire", compute="_compute_n_salaire", strore=True)

    @api.depends('salaire', 'multiplier')
    def _compute_n_salaire(self):
    	for record in self:
    		if record.multiplier == 'DOUBLE':
    			record.n_salaire = record.salaire * 2
    		elif record.multiplier == 'TRIPLE':
    			record.n_salaire = record.salaire * 3
    		else:
    			record.n_salaire = record.salaire
    		

    # ch = fields.Integer(string="ch", compute=vie)

    # def VIE(self):
    # 	self.ch = len(self.ch)

#  pname = fields.Char(compute='_compute_pname')

# @api.one
# @api.depends('partner_id.name', 'partner_id.is_company')
# def _compute_pname(self):
#     if self.partner_id.is_company:
#         self.pname = (self.partner_id.name or "").upper()
#     else:
#         self.pname = self.partner_id.name