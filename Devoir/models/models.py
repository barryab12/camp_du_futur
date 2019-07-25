# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Etudiant(models.Model):
    _name = 'model.etudiant'

    name = fields.Char(string="Nom")
    prenom = fields.Char(string="Prénopm(s)")
    niveau = fields.Selection(string="Niveau", selection=[('L1','Licence 1'),('L2','Licence 2'),('L3','Licence 3')])
    filiere = fields.Selection(string="Filière", selection=[('SI','SEI / IIM'),('RT','RIT / TCOM'),('II','IDA / IG')])
    student = fields.Many2one('res.users', string="student")
    # texte = fields.Char(default="Veuillez cliqueer sur le bouton ci-dessous pour déposer votre devoir", readonly=True)
    # mon_devoir = fields.One2many('model.depot', 'etudiant')
    # file_name = fields.Char(string="File Name")
    nb_note = fields.One2many('model.depot', 'etudiant')
    note = fields.Char(string="Note", compute='_note', readonly=True)

    @api.onchange('nb_note')
    @api.multi
    def _note(self):
        i = 0
        for rec in self:
            for n in rec.nb_note:
                if n !='':
                    i += 1
        rec.note = str(i)+" / 5"
    
class Depot_devoir(models.TransientModel):
    _name = 'model.depot'

    # devoir = fields.Binary(string="Charger un fichier", store=True)
    # nom_fichier = fields.Char(string="Nom du fichier")
    student = fields.Many2one('res.users', string="student")
    etudiant = fields.Many2one('model.etudiant', 'Votre nom')
    note = fields.Selection(string="Note", default="0", selection=[('n0','0'),('n1','1'),('n2','2'),('n3','3'),('n4','4'),('n5','5'),('n6','6'),('n7','7'),('n8','8'),('n9','9'),('n10','10')], required=True, store=True)
