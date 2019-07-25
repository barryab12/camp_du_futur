# -*- coding: utf-8 -*-
from odoo import models, fields, api
 
class notation(models.Model):
    _name = 'model.notation'
    _rec_name = ("candidat")

    note = fields.Char(string="Note", required=True)
    candidat  = fields.Many2one(commodel_name="res.users", string="candidat" , domain=[('model.notation','in',[5])])