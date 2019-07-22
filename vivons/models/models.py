# -*- coding: utf-8 -*-
    
from odoo import models, fields, api
from random import *

class ExtraitPere(models.Model):
    _name = 'mod.pere'

    nom = fields.Char(string="Nom", default="" ,required=True )
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    matricule = fields.Char(string="Matricule", compute='_vie', store=True)
    photo = fields.Binary(string="Photo")
    myri = fields.One2many(comodel_name= 'mod.extrait', inverse_name='pere')

    @api.multi
    def name_get(self):
        result = []
        for modpere in self:
            name = (modpere.nom + ' ' + modpere.prenom)
            result.append((modpere.id, name))
        return result

    @api.depends('nom', 'matricule')
    def _vie(self):
        for record in self:
            record.matricule = record.nom[:3].upper() + str(randrange(99999))


class ExtraitMere(models.Model):
    _name = 'mod.mere'
    
    

    nom = fields.Char(string="Nom", default="" , required=True)
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    matricule = fields.Char(string="Matricule", compute='vie', store=True)
    photo = fields.Binary(string="Photo")
    myri = fields.One2many(comodel_name= 'mod.extrait', inverse_name='mere')

    @api.multi
    def name_get(self):
        result = []
        for modmere in self:
            name = (modmere.nom + ' ' + modmere.prenom)
            result.append((modmere.id, name))
        return result

    @api.depends('nom', 'matricule')
    def vie(self):
        for record in self:
            record.matricule = record.nom[:3].upper() + str(randrange(99999))






class Extrait(models.Model):
    _name = 'mod.extrait'

    n = fields.Char(string="Nom", required=True)
    p = fields.Char(string="Prénom(s)", required=True)
    dn = fields.Date(string="Date de naissance", default=fields.Date.today)
    ville_n = fields.Char(string="Ville de naissance")
    pere = fields.Many2one(comodel_name="mod.pere", string="Père")
    mere = fields.Many2one(comodel_name="mod.mere", string="Mère")
    matricule = fields.Char(string="Matricule", compute='_mii', store=True)
    attachment_ids = fields.Many2many('ir.attachment', string="upload")
    file_name = fields.char(string="file name")

    @api.depends('n', 'matricule')
    def _mii(self):
        for record in self:
            record.matricule = record.pere.nom[:2].upper() + record.mere.nom[:2].upper() + str(randrange(99999))

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