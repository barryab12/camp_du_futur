from odoo import models, fields

class NouveauModele(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'
 
    commentaire = fields.Char(string="votre commentaire", required=True)

    selection = fields.Selection(string="selection", selection=[('OUI','oui'),('NON','non')])

    many = fields.Many2one(comodel_name="fleet.vehicle.model", string="vehicle")
