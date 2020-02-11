# -*- coding: utf-8 -*-
# from odoo import http


# class XtestModule(http.Controller):
#     @http.route('/xtest_module/xtest_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xtest_module/xtest_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xtest_module.listing', {
#             'root': '/xtest_module/xtest_module',
#             'objects': http.request.env['xtest_module.xtest_module'].search([]),
#         })

#     @http.route('/xtest_module/xtest_module/objects/<model("xtest_module.xtest_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xtest_module.object', {
#             'object': obj
#         })
