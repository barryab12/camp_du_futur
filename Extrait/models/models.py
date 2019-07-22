# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import randint
from random import randrange

class ExtraitPere(models.Model):
    _name = 'mod.pere'
    _rec_name = 'nom'

    nom = fields.Char(string="Nom", required=True, default="")
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    matricule = fields.Char(string="votre matricule", compute="_matricule", readonly=True, store=True)
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")
    enfant = fields.One2many(comodel_name="mod.extrait", inverse_name="pere")


    @api.multi
    def name_get(self):
        res = []
        for ExtraitPere in self:
            name = ExtraitPere.nom +' '+ ExtraitPere.prenom
            res.append((ExtraitPere.id, name))
        return res

    @api.depends('nom', 'matricule')
    def _matricule(self):
        self.matricule = self.nom[:3].upper() +str(randrange(99999))

    # @api.depends('salaire', 'multiplier')
    # def _poolet(self):
    #   for record in self:
    #       if record.nom == record.Extrait.pere.nom
    #           record.pool = record.salaire * 2
    #       elif record.multiplier == 'TRIPLE':
    #           record.n_salaire = record.salaire * 3
    #       else:
    #           record.n_salaire = record.salaire
        


class ExtraitMere(models.Model):
    _name = 'mod.mere'
    _rec_name = 'nom'

    nom = fields.Char(string="Nom", required=True, default="")
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    matricule = fields.Char(string="votre matricule", compute="_matricule", readonly=True, store=True)
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")

    @api.multi
    def name_get(self):
        res = []
        for ExtraitMere in self:
            name = ExtraitMere.nom +' '+ ExtraitMere.prenom
            res.append((ExtraitMere.id, name))
        return res

    @api.depends('nom', 'matricule')
    def _matricule(self):
        self.matricule = self.nom[:3].upper() +str(randrange(99999))

class Extrait(models.Model):
    _name = 'mod.extrait'
    _rec_name = 'nom'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom(s)", required=True)
    dn = fields.Date(string="Date de naissance", default=fields.Date.today)
    ville_n = fields.Char(string="Ville de naissance")
    matricule = fields.Char(string="votre matricule", compute="_matricule", readonly=True, store=True)
    pere = fields.Many2one(comodel_name="mod.pere", string = "pere")
    mere = fields.Many2one(comodel_name="mod.mere", string="Mère")

    @api.multi
    def name_get(self):
        res = []
        for Extrait in self:
            name = Extrait.nom +' '+ Extrait.prenom
            res.append((Extrait.id, name))
        return res


    @api.depends('nom','matricule')
    def _matricule(self):
        for rec in self:
            per = rec.pere.nom[:2]
            mer = rec.mere.nom[:2]
            # mer = rec.mare.nom[:2]
            b = ''
            while len(b) < 5:
                mat = randint(0,9)
                b += str(mat)
            rec.matricule = per.upper() + mer.upper() + b
    

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