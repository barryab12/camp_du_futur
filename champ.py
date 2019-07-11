from odoo import models, fields, api

class NouveauChamp(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'
    # Creation du champ age
    salaire = fields.Integer(string="Votre salaire")
    multiplier = fields.Selection(string="Multiplier", selection=[(2,'Doubler'),(3,'Tripler')])
    # employ = fields.Many2one(comodel_name="hr.employee", string='Employé(e)')
    nouveauSalaire =fields.Integer(string="Nouveau salaire", compute='multi', readonly=True)

    @api.depends('salaire','multiplier')
    def multi(self):
    	for record in self:
    		if record.multiplier == 2:
    			record.nouveauSalaire = record.salaire * 2
    		elif record.multiplier == 3:
    			record.nouveauSalaire = record.salaire * 3
    		else:
    			record.nouveauSalaire = record.salaire