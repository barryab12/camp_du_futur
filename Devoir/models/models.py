# -*- coding: utf-8 -*-

from odoo import models, fields, api
#from datetime import datetime
#from random import *

class EtudiantEtudiant(models.Model):
    _name = 'etudiant.etudiant'
    _rec_name =( "note")

    nom = fields.Many2one(comodel_name ="res.users" ,string =  "nom")
    note = fields.Char(string="note", required=True)

    @api.depends('note')
    @api.multi
    def _note(self):
        i = 0
        for rec  in self:
            for x in rec.note:
                if x != '':
                    i += 1
        rec.note = str(i)

    #name = fields.Char(string="Nom", required=True)
    #prenom = fields.Char(string="Prénopm(s)", required=True)
    #niveau = fields.Selection(string="Niveau", selection=[('L1','Licence 1'),('L2','Licence 2'),('L3','Licence 3')])
    #filiere = fields.Selection(string="Filière", selection=[('SI','SEI / IIM'),('RT','RIT / TCOM'),('II','IDA / IG')])
   # texte = fields.Char(default="Veuillez cliqueer sur le bouton ci-dessous pour déposer votre devoir", readonly=True)
   # mon_devoir = fields.One2many('model.depot', 'etudiant')
   # note = fields.Char(string= "Note", readonly=True)
    # file_name = fields.Char(string="File Name")
    
#class Depot_devoir(models.TransientModel):
    #_name = 'model.depot'

    #devoir = fields.Binary(string="Charger un fichier", store=True)
#nom_fichier = fields.Char(string="Nom du fichier")
    #etudiant = fields.Many2one('model.etudiant', 'Votre nom')
