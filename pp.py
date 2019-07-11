from odoo import models, fields

class Tache(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    love = fields.Selection(string ="Aimez vous cette entreprise ?", selection=[('oui','OUI'),('non','NON')])
    rapport = fields.Many2one(comodel_name='project.project', string="Projet Attribué")