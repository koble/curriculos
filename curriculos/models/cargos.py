# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _

class cargos(models.Model):
     _name             = 'curriculos.cargos'
     _description      = u'Cargos'
     _order            = 'name'
     _sql_constraints  = {
         ('name_area',
          'UNIQUE(name,area_funcional_id)',
          u'O Cargo não pode se repetir na mesma Área Funcional!'
         )
     }

     name              = fields.Char(
         string=u'Cargo',
     )
     area_funcional_id = fields.Many2one(
         'curriculos.areas_funcionais',
         default=lambda self: self._context.get('area_funcional'),
         string=u'Área Funcional',
         ondelete='restrict',
     )
     experiencias_ids = fields.One2many(
         'curriculos.experiencias',
         'cargos_id',
         ondelete='restrict',
     )
