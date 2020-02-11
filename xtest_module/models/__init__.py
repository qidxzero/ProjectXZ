# -*- coding: utf-8 -*-

from . import models, fields, api

class Course(models.Model):
    _name = 'xtest.course'
    _description = "xtest module creation for Odoo development"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
