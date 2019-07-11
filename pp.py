from odoo import models, fields, api

class Tache(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    salaire = fields.Integer(string ="Votre Salaire",required = True)
    Multiplier = fields.Selection(string ="Multiplier",selection=[('DOUBLER','doubler'),('TRIPLER','tripler')])
    NouSalaire = fields.Integer(string ="Nouveau_Salaire", compute='_compute_NouSalaire', store=True)

    @api.depends('salaire','Multiplier')
    def _compute_NouSalaire(self):
        for record in self:
            if record.Multiplier == 'DOUBLER' :
                record.NouSalaire = record.salaire * 2
            elif record.Multiplier == 'TRIPLER' :
                record.NouSalaire = record.salaire * 3
            else :
                record.NouSalaire = record.salaire
