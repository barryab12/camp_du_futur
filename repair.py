from odoo import models, fields

class NouveauModele(models.Model):
    _name = 'repair.order'
    _inherit = 'repair.order'
    
    probleme = fields.Selection(string="Problème rencontré",selection=[('SOFTWARE','Logiciel'),('MATERIAL','Matériel')])

    info = fields.Many2one(comodel_name="account.payment", string='Methode de payement', required=True)