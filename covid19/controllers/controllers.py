# -*- coding: utf-8 -*-
from odoo import http

# class Covid19(http.Controller):
#     @http.route('/covid19/covid19/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/covid19/covid19/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('covid19.listing', {
#             'root': '/covid19/covid19',
#             'objects': http.request.env['covid19.covid19'].search([]),
#         })

#     @http.route('/covid19/covid19/objects/<model("covid19.covid19"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('covid19.object', {
#             'object': obj
#         })