# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import *

class Etudiant(models.Model):
    _name = 'model.etudiant'

    name = fields.Char(string="Nom", required=True, store=True)
    prenom = fields.Char(string="Prénopm(s)", required=True)
    niveau = fields.Selection(string="Niveau", selection=[('L1','Licence 1'),('L2','Licence 2'),('L3','Licence 3')])
    filiere = fields.Selection(string="Filière", selection=[('SI','SEI / IIM'),('RT','RIT / TCOM'),('II','IDA / IG')])
    # texte = fields.Char(default="Veuillez cliqueer sur le bouton ci-dessous pour déposer votre devoir", readonly=True)
    # mon_devoir = fields.One2many('model.depot', 'etudiant')
    # file_name = fields.Char(string="File Name")
    nb_note = fields.One2many('model.depot', 'etudiant', store=True)
    note = fields.Char(string="Note", compute='_note', readonly=True, store=True)
    
    iden = fields.Integer(string="Copie Identifiant", default=lambda self: self._context.get('active_ids'), readonly=True, store=True)

    @api.onchange('nb_note')
    @api.multi
    def _note(self):
        i = 0
        for rec in self:
            for n in rec.nb_note:
                if n != '':
                    i += 1
        rec.note = str(i)+" / 5"

    @api.multi
    def _iden(self):
        for c in self:
            c.iden = c._context.get('active_id')
    
class Depot_devoir(models.TransientModel):
    _name = 'model.depot'

    # devoir = fields.Binary(string="Charger un fichier", store=True)
    # nom_fichier = fields.Char(string="Nom du fichier")
    iden_can = fields.Char('Id name', default=lambda self: self.env['model.etudiant'])
    etudiant = fields.Many2one('model.etudiant', 'Votre nom', domain=[('name','!=','iden_can')], required=True)
    note = fields.Selection(string="Note", selection=[('n0','0'),('n1','1'),('n2','2'),('n3','3'),('n4','4'),('n5','5')], default="0", required=True, store=True)
