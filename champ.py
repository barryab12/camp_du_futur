from odoo import models, fields

class NouveauChamp(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'
    # Creation du champ age
    num = fields.Integer(string="Numéro", required=True)