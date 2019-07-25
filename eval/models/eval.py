# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Candidat(models.Model):
    _name = 'candidat.candidat'

    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénopm(s)", required=True)
    niveau = fields.Selection(string="Niveau", selection=[('L1','Licence 1'),('L2','Licence 2'),('L3','Licence 3')])
    filiere = fields.Selection(string="Filière", selection=[('SI','SEI / IIM'),('RT','RIT / TCOM'),('II','IDA / IG')])
    # texte = fields.Char(default="Veuillez cliqueer sur le bouton ci-dessous pour déposer votre devoir", readonly=True)
    # mon_devoir = fields.One2many('model.depot', 'etudiant')
    # file_name = fields.Char(string="File Name")
    nb_note = fields.One2many('depot.depot', 'etudiant')
    note = fields.Char(string="Note", compute='_note', readonly=True)

    @api.onchange('nb_note')
    @api.multi
    def _note(self):
        i = 0
        for rec in self:
            if rec.nb_note.note != None:
                i += 1
        rec.note = str(i)+" / 5"

class Depot_devoir(models.TransientModel):
    _name = 'depot.depot'

    # devoir = fields.Binary(string="Charger un fichier", store=True)
    # nom_fichier = fields.Char(string="Nom du fichier")
    student = fields.Many2one('res.users', string="student")
    etudiant = fields.Many2one('model.etudiant', 'Votre nom', required=True)
    note = fields.Selection(string="Note", selection=[('n1','1'),('n2','2'),('n3','3'),('n4','4'),('n5','5')], required=True, store=True)
