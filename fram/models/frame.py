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
    note = fields.Selection(string='Note',selection=[('0', '0'), ('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),('16', '16'),('17', '17'),('18', '18')])

    @api.depends('note')
    @api.multi
    def _note(self):
        i = 0
        for rec in self:
            for x in rec.note:
                if x != '':
                    i += 1
        rec.note = str(i)