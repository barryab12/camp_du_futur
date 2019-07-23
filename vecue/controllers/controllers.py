# -*- coding: utf-8 -*-
from odoo import http

# class MonModule(http.Controller):
#     @http.route('/mon_module/mon_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mon_module/mon_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mon_module.listing', {
#             'root': '/mon_module/mon_module',
#             'objects': http.request.env['mon_module.mon_module'].search([]),
#         })

#     @http.route('/mon_module/mon_module/objects/<model("mon_module.mon_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mon_module.object', {
#             'object': obj
#         })