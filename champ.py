from odoo import models, fields

class NouveauChamp(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'
    # Creation du champ age
    num = fields.Integer(string="Numéro", required=True)
    genre = fields.Selection(string="Genre", selection=[('M','Masculin'),('F','Féminin')])
    employ = fields.Many2one(comodel_name="hr.employee", string='Employé(e)')