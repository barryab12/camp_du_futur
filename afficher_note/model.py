from odoo import fields, models, api

class Afficher_note(models.Model):
    _name = 'op.student'
    _inherit = 'op.student'

    notes = fields.Char('Record', compute='nombre_note', readonly=True)

    @api.onchange('note')
    def nombre_note(self):
        for rec in self:
            rec.notes = lambda self: self.env['op.note'].search([('etudiant','=',self.env.user.name)])

class Notes(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    notes = fields.One2many('op.note', 'etudiant', 'Notes', readonly=True)
    nb_note = fields.Char('Nombre de note obtenue', default="", compute='etudiant_note', readonly=True)

    @api.onchange('notes')
    @api.multi
    def etudiant_note(self):
        i = 0
        for rec in self:
            for n in range(len(rec.notes)):
                i += 1
        self.nb_note = str(i)
    