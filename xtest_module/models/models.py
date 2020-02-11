# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class xtest_module(models.Model):
#     _name = 'xtest_module.xtest_module'
#     _description = 'xtest_module.xtest_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
