# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from random import *

class ExtraitPere(models.Model):
    _name = 'mod.pere'
    _rec_name = 'matricule'

    nom = fields.Char(string="Nom", default="", required=True)
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")
    matricule = fields.Char(string="Matricule", compute='_mat', readonly=True, store=True)

    @api.multi
    def name_get(self):
        res = []
        for data in self:
            name = data.nom+' '+data.prenom
            res.append((data.id, name))
        return res
    
    @api.depends('nom')
    def _mat(self):
        self.matricule = self.nom[0:3].upper() + str(randrange(99999))

class ExtraitMere(models.Model):
    _name = 'mod.mere'
    _rec_name = 'matricule'

    nom = fields.Char(string="Nom", default="", required=True)
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")
    matricule = fields.Char(string="Matricule", compute='_mat', readonly=True, store=True)

    @api.multi
    def name_get(self):
        res = []
        for data in self:
            name = data.nom+' '+data.prenom
            res.append((data.id, name))
        return res

    @api.depends('nom')
    def _mat(self):
        self.matricule = self.nom[0:3].upper() + str(randrange(99999))

class Extrait(models.Model):
    _name = 'mod.extrait'
    _rec_name = 'matricule'

    nom = fields.Char(string="Nom", default="", required=True)
    prenom = fields.Char(string="Prénom(s)", required=True)
    dn = fields.Date(string="Date de naissance", default=fields.Date.today)
    ville_n = fields.Char(string="Ville de naissance")
    pere = fields.Many2one(comodel_name="mod.pere", default="", string="Père")
    mere = fields.Many2one(comodel_name="mod.mere", default="", string="Mère")
    matricule = fields.Char(string="Matricule", compute='_mat', readonly=True, store=True)

    @api.multi
    def name_get(self):
        res = []
        for data in self:
            name = data.nom+' '+data.prenom
            res.append((data.id, name))
        return res

    @api.depends('nom')
    def _mat(self):
        self.matricule = self.pere.nom[0:2].upper() + self.mere.nom[0:2].upper() + str(randrange(99999))
        
    

# class ExtraitPdf(models.AbstractModel):
#     _name = 'mod.extraitpdf'
#     @api.model
#     def render_pdf(self, docids, data=None):
#         report_obj = self.env['report']
#         report = report_obj._get_report_from_name('module.report_name')
#         docargs = {
#             'doc_ids': docids,
#             'doc_model': report.model,
#             'docs': self,
#         }
#         return report_obj.render('module.report_name', docargs)