# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Candidat(models.Model):
    _name = 'op.student'
    _inherit = 'op.student'
    
    nb_note = fields.One2many('op.student.noter', 'cand', string="Noteur", store=True)
    note_info = fields.Char(string="Info Note", compute='_note', readonly=True, store=True)
    moy = fields.Float(string="Moyenne", digits=(1, 2), compute='_moy', readonly=True)

    @api.onchange('nb_note')
    @api.multi
    def _note(self):
        i = 0
        res =""
        for rec in self:
            for n in rec.nb_note:
                for m in n.note:
                    if i == 5:
                        res = "Vous avez été noté !"
                        rec.note_info = res
                        break
                    else:
                        res = "Vous êtes entrain d'être noté ......"
                        rec.note_info = res
                        i += 1
    
    def _moy(self):
        i = 0
        note = 0
        for rec in self:
            for n in rec.nb_note:
                for nte in n.note:
                    if i == 5:
                        rec.moy = note / 5
                        break
                    else:
                        i += 1
                        note += int(nte)
        

class Select_User(models.Model):
    _inherit = 'res.users'

    is_student = fields.Boolean(string="Etudiant ?", default=False, compute='check_if_is_student')

    @api.depends('user_line', 'name')
    def check_if_is_student(self):
        for rec in self:
            if rec.user_line != rec.name:
                rec.is_student = True
            else:
                rec.is_student = False


class Noter(models.TransientModel):
    _name = 'op.student.noter'

    cand = fields.Many2one('res.users', 'Etudiants', domain=[('is_student','=','True')], required=True)
    note = fields.Selection(string="Note", selection=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], default='0', required=True, store=True)
    noteur = fields.Char(string="Noter par", default=lambda self: self.env.user.name, readonly=True, store=True)
    id_noteur = fields.Char(string="Identifiant noteur", default=lambda self: self.env.uid, readonly=True, store=True)