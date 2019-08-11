# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _

class linguas(models.Model):
     _name             = 'curriculos.linguas'
     _description      = u'Línguas'
     _order            = 'name'

     name              = fields.Char(
         string=u'Língua',
     )
     linguas_curriculos_rel_ids = fields.One2many(
         'curriculos.linguas_curriculos_rel',
         'linguas_ids',
     )
