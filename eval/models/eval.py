# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import *

class Candidat(models.Model):
    _name = 'candidat.candidat'

    name = fields.Char(string="Nom", required=True, store=True)
    prenom = fields.Char(string="Prénopm(s)", required=True)
    niveau = fields.Selection(string="Niveau", selection=[('L1','Licence 1'),('L2','Licence 2'),('L3','Licence 3')])
    filiere = fields.Selection(string="Filière", selection=[('SI','SEI / IIM'),('RT','RIT / TCOM'),('II','IDA / IG')])
    note_chif = fields.One2many('model.depot', 'etudiant', store=True)
    note = fields.Char(string="Note", compute='_note', readonly=True, store=True)

    identifiant = fields.Integer(string="Copie identifiant", default=lambda self: self._context.get('active_ids'), readonly=True, store=True)

    @api.onchange('note_chif')
    @api.multi
    def _note(self):
        i = 0
        for rec in self:
            for n in rec.note_chif:
                if n != '':
                    i += 1
        rec.note = str(i)+" / 5"

    @api.multi
    def _identifiant(self):
        for c in self:
            c.identifiant = c._context.get('active_id')

class Depot(models.TransientModel):
    _name = 'depot.depot'

    # devoir = fields.Binary(string="Charger un fichier", store=True)
    # nom_fichier = fields.Char(string="Nom du fichier")
    identifiant_can = fields.Char('Id name', default=lambda self: self.env['model.etudiant'])
    candidat = fields.Many2one('candidat.candidat', 'Votre nom', domain=[('name','!=','identifiant_can')], required=True)
    note = fields.Selection(string="Note", selection=[('A','0 - 5'),('B','5-10'),('C','10-15'),('D','15-20')], default="0", required=True, store=True)
