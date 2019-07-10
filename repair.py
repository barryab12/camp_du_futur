from odoo import models, fields

class NouveauModele(models.Model):
    _name = 'repair.order'
    _inherit = 'repair.order'
    
    probleme = fields.Char(string="Problème rencontré", required=True)