from odoo import models, fields, api

class NouveauModele(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    salaire = fields.Integer(string="votr salaire", required=True)
    multiplier = fields.Selection(string= "Multripler valeurs ?", selection=[('DOUBLER','doubler'),('TRIPLER','tripler')])
    nv_salaire = fields.Integer(string="nouveau salaire", compute= "_compute_nv_salaire", readonly=True)

    @api.depends('salaire' ,'multiplier')
    def _compute_nv_salaire(self):
        for record in self :
            if record.multiplier == 'DOUBLER':
                record.nv_salaire = record.salaire * 2
                
            elif record.multiplier == 'TRIPLER':
                record.nv_salaire = record.salaire * 3
            
            else:
                record.nv_salaire = record.salaire
