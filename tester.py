from odoo import models, fields

class ComputedModel(models.Model):
     _name = 'sale.order.form'
     _inherit = 'sale.order.form'
     numero = fields.Char(string = "votre numero",required = True)

        