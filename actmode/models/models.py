# -*- coding: utf-8 -*-

from odoo import models, fields ,api 
from random import randint

class ExtraitPere(models.Model):
    _name = 'mod.pere'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")
    matricule=fields.Char(string = "Matricule",compute= '_matri',readonly= True)

    @api.depends('nom','matricule')
    def _matri(self):
        for rec in self:
            lettre = rec.nom[:3]
            b = ''
            while len(b) < 5:
                matri = randint(0,9)
                b += str(matri)
            rec.matricule = lettre.upper() + b
    
    @api.multi
    def name_get(self):
        result = []
        for modpere in self:
            name = modpere.nom +' '+ modpere.prenom
            result.append((modpere.id, name))
        return result

class ExtraitMere(models.Model):
    _name = 'mod.mere'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")
    matricule=fields.Char(string = "Matricule",compute= '_matri',readonly= True)

    @api.depends('nom','matricule')
    def _matri(self):
        for rec in self:
            lettre = rec.nom[:3]
            b = ''
            while len(b) < 5:
                mat = randint(0,9)
                b += str(mat)
                rec.matricule = lettre.upper() + b

    @api.multi
    def name_get(self):
        result = []
        for modmere in self:
            name = modmere.nom +' '+ modmere.prenom
            result.append((modmere.id, name))
        return result

class Extrait(models.Model):
    _name = 'mod.extrait'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom(s)", required=True)
    dn = fields.Date(string="Date de naissance", default=fields.Date.today)
    ville_n = fields.Char(string="Ville de naissance")
    pere = fields.Many2one(comodel_name="mod.pere", string="Père")
    mere = fields.Many2one(comodel_name="mod.mere", string="Mère")
    matricule=fields.Char(string = "Matricule",compute= '_matri',readonly= True)
    
    @api.depends('nom','matricule')
    def _matri(self):
        for rec in self:
            lettre = rec.nom[:3]
            b = ''
            while len(b) < 5:
                matri = randint(0,9)
                b += str(matri)
                rec.matricule = lettre.upper() + b