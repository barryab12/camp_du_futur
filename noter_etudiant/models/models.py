from odoo import fields, models, api

class Note(models.Model):
    _name = 'op.note'

    etudiant = fields.Many2one('res.users', 'Etudiant', domain=lambda self: [('id','!=',2),('id','!=',self.env.uid)], required=True)
    note = fields.Selection(string='Note', selection=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),], default='0', required=True)



    