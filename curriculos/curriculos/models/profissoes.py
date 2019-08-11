# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _

class profissoes(models.Model):
     _name             = 'curriculos.profissoes'
     _description      = u'Profissões'
     _order            = 'name'
     _sql_constraints  = {
         ('name_area',
          'UNIQUE(name)',
          u'A Profissão não pode ser repetida!'
         )
     }

     name              = fields.Char(
         string=u'Profissão',
     )
     curriculos_ids    = fields.One2many(
         'curriculos.curriculos',
         'profissoes_id',
         string='Currículos',
     )
