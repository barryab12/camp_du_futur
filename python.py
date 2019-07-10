from odoo import models, fields

class NouveauModele(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    
    nationalite = fields.Selection(string="nationalite",selection=[('Ivoirien'),('Etranger')])
    probleme = fields.Many2one(comodel_name="purchase.order", string="achats")