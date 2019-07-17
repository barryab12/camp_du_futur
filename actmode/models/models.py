# -*- coding: utf-8 -*-

from odoo import models, fields

class ExtraitPere(models.Model):
    _name = 'mod.pere'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")

class ExtraitMere(models.Model):
    _name = 'mod.mere'

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénoms", required=True)
    dn = fields.Date(string="Date de naissance")
    ville_n = fields.Char(string="Ville de naissance")
    prof = fields.Char(string="Profession")
    photo = fields.Binary(string="Photo")

class Extrait(models.Model):
    _name = 'mod.extrait'

    n = fields.Char(string="Nom", required=True)
    p = fields.Char(string="Prénom(s)", required=True)
    dn = fields.Date(string="Date de naissance", default=fields.Date.today)
    ville_n = fields.Char(string="Ville de naissance")
    pere = fields.Many2one(comodel_name="mod.pere", string="Père")
    mere = fields.Many2one(comodel_name="mod.mere", string="Mère")
    

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