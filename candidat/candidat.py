# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Candidat(models.Model):
    _name = 'op.student'
    _inherit = 'op.student'
    
    nb_note = fields.One2many('op.student.noter', 'cand', string="Noteur", store=True)
    note_info = fields.Char(string="Info Note", readonly=True, store=True)                   

class Noter(models.TransientModel):
    _name = 'op.student.noter'

    noteur = fields.Char(string="Noter par", default=lambda self: self.env.user.name, readonly=True, store=True)
    cand = fields.Many2one('res.users', 'Etudiants', domain=[('name','!=','Administrator')], required=True)
    note = fields.Selection(string="Note", selection=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], default='0', required=True, store=True)
    id_noteur = fields.Char(string="Identifiant noteur", default=lambda self: self.env.uid, readonly=True, store=True)
    etudiant_note = fields.Char(string="Etudiant noté", compute='get_student_name', readonly=True, store=True)

    @api.depends('cand')
    def get_student_name(self):
        for r in self:
            r.etudiant_note = r.cand.name
    

class Info(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    info = fields.One2many('op.student.noter', 'cand', string="Informations", readonly=True, store=True)
    info_note = fields.Char('Votre note', compute='_note', readonly=True)
    moy = fields.Float(string="Moyenne", digits=(1, 2), compute='_moy', readonly=True)
        

    @api.onchange('info')
    @api.multi
    def _note(self):
        i = 0
        res =""
        nb_pers = str(i) + " / 5"
        for rec in self:
            for n in rec.info:
                for m in n.note:
                    if i == 5:
                        res = nb_pers + "   Vous avez été noté !"
                        break
                    else:
                        i += 1
                        res = nb_pers + "   Vous êtes entrain d'être noté ......"
        rec.info_note = res

    def _moy(self):
        i = 0
        note = 0
        for rec in self:
            for n in rec.info:
                for nte in n.note:
                    if i >= 5:
                        rec.moy = note / 5
                        break
                    else:
                        i += 1
                        note += int(nte)