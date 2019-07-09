from odoo import models, fields

class NouveauModele(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'
    # Creation du champ age
    commentaire = fields.Char(string="Votre commentaire", required=True)