from odoo import models, fields

class NouveauModele(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    numero = fields.Integer(string="numero", required=True)
    value = fields.Selection(string= "Ville", selection=[('Ville','ville'),('Paris','paris')])
    Many_2one = fields.Many2one(comodel_name= "res.partner", string= "Contact")
    #    value = fields.selection(string="Votre ville", selection=[('VILLE','ville'),('PARIS','paris')])