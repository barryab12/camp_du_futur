from odoo import models, fields, api

class NouveauModele(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    salaire = fields.Integer(string= "votre salaire",required = True) 

    multiplier = fields.Selection(string= "multiplier",selection=[('DOUBLER','doubler'),('TRIPLER','tripler')])

    nouveau_salaire = fields.Integer(string= "nouveau_salaire",compute='_compute_nouveau_salaire',store = True) 
    # compute empeche de saisir

    @api.depends('salaire', 'multiplier')
    def _compute_nouveau_salaire(self):
        for r in self:
            if  r.multiplier == 'DOUBLER':
                r.nouveau_salaire = r.salaire * 2

            elif r.multiplier == 'TRIPLER':
                r.nouveau_salaire = r.salaire * 3

            else:
                r.nouveau_salaire = r.salaire