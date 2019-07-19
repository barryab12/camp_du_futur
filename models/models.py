# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import randrange

class ExtraitPere(models.Model):
    _name = 'mod.pere'

    nom = fields.Char(string="Nom")
    prenom = fields.Char(string="Prénoms")
    matricule = fields.Char(string= "Matricule",compute='_matricule',Readonly=True, store=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")

    @api.depends('nom')
    def _matricule(self):
        for r in self:
            r.matricule = r.nom[:3].upper() + str((randrange)(99999))



    @api.multi
    def name_get(self):
            result = []
            for modpere in self:
                name = str(modpere.nom + ' ' + modpere.prenom)
                result.append((modpere.id, name))
            return result

    

class ExtraitMere(models.Model):
    _name = 'mod.mere'

    nom = fields.Char(string="Nom")
    prenom = fields.Char(string="Prénoms")
    matricule = fields.Char(string="matricule",compute='_matricule',Readonly=True,store=True) 
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")



    
    @api.depends('nom')
    def _matricule(self):
        for r in self:
            r.matricule = r.nom[:3].upper()  + str((randrange)(99999))




    
    @api.multi
    def name_get(self):
        result = []
        for modmere in self:
            name = str(modmere.nom + ' ' + modmere.prenom)
            result.append((modmere.id, name))
        return result



class Extrait(models.Model):
    _name = 'mod.extrait'

    nom = fields.Char(string="Nom")
    prenom = fields.Char(string="Prénom(s)")
    matricule = fields.Char(string= "matricule",compute='_matricule',Readonly=True,store=True)
    dn = fields.Date(string="Date de naissance", default=fields.Date.today)
    ville_n = fields.Char(string="Ville de naissance")
    pere = fields.Many2one(comodel_name="mod.pere", string="Père")
    mere = fields.Many2one(comodel_name="mod.mere", string="Mère")


    @api.depends('nom')
    def _matricule(self):
        for r in self:
            a = r.pere.nom[:2]
            b = r.mere.nom[:2]
            e = a + b
            c = ''
            while len(c) < 5:
                d = (randrange)(99999)
                c += str(d)
            r.matricule =e.upper() + c 

    @api.multi
    def name_get(self):
        result = []
        for modextrait in self:
            name = str(modextrait.nom + ' ' + modextrait.prenom)
            result.append((modextrait.id, name))
            return result





                

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