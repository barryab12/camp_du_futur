from odoo import models, fields, api

class NouveauModele(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    # Creation du champ type_de_carte
    votre_salaire = fields.Integer(string="votre salaire", required=True)
    multiplier = fields.Selection(string="multiplier", selection=[('1','Doubler'), ('2','Tripler')])
    #employee = fields.Many2one(comodel_name="hr.employee", string="employé")
    nouveau_salaire = fields.Integer(string="Nouveau salaire", compute="_compute_choix", readonly=True) 
   
    @api.depends('votre_salaire','multiplier')
    def _compute_choix(self):
        for r in self:
            if r.multiplier == '1':
                r.nouveau_salaire = r.votre_salaire * 2
            elif r.multiplier == '2':
                r.nouveau_salaire = r.votre_salaire * 3
            else :
                r.nouveau_salaire = r.votre_salaire

