# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import *

class Utilisateur(models.Model):
    _inherit = 'res.users'
    
    nb_note = fields.One2many('candidat.noter', 'cand', store=True)
    note_info = fields.Char(string="Info Note", compute='_note', readonly=True, store=True)
    moy = fields.Integer(string="Moyenne", compute='_moy', readonly=True)

    @api.onchange('nb_note')
    @api.multi
    def _note(self):
        i = 0
        for rec in self:
            for n in rec.nb_note:
                if n != '':
                    if i == 5:
                        res = "Vous avez été noté !"
                        break
                    else:
                        res = "Vous êtes entrain d'être noté ......"
                        i += 1
                        note += int(n.note)
        rec.moy = note / 5
        rec.note = res
    
    def _moy(self):
        i = 0
        for rec in self:
            for n in rec.nb_note:
                if n != '':
                    if i == 5:
                        break
                    else:
                        i += 1
                        note += int(n.note)
        rec.moy = note / 5
        
    
class Noter(models.TransientModel):
    _name = 'candidat.noter'

    # devoir = fields.Binary(string="Charger un fichier", store=True)
    # nom_fichier = fields.Char(string="Nom du fichier")
    # iden_can = fields.Char('Id name', default=lambda self: self.env.uid)
    cand = fields.Many2one('res.users', 'Candidat', required=True)
    note = fields.Selection(string="Note", selection=[('n0','0'),('n1','1'),('n2','2'),('n3','3'),('n4','4'),('n5','5')], default="0", required=True, store=True)
    noteur = fields.Char(default=lambda self: self.env.user.name, readonly=True)