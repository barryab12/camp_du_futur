# -*- coding: utf-8 -*-

from odoo import models, fields,api
from random import *

class InscriptionInscription(models.Model):
    _name = 'mod.inscription'

    name = fields.Char(string='Nom', default="", required=True)
    prenom = fields.Char(string='Prenoms', required=True)
    matricule = fields.Char(string='Matricule', compute='_mat', readonly=True, store=True)
    niveau = fields.Selection(string="Niveau", selection=[('L1','Licence 1'),('L2','Licence 2'),('L3','Licence 3')])
    filiere = fields.Selection(string="Filière", selection=[('SI','SEI / IIM'),('RT','RIT / TCOM'),('II','IDA / IG')])

    @api.depends('name')
    def _mat(self):
        for rec in self:
            laa = rec.nom[:3]
            s = ''
            while len(s) < 4:
                mit = randint(0,9)
                s += str(mit)
        rec.matricule = laa.upper() + s
    

class NoterNoter(models.Model):
    _name = 'mod.noter'

    nom = fields.Many2one(comodel_name="res.users", string='Nom')