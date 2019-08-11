# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _

class empresas(models.Model):
     _name             = 'curriculos.empresas'
     _description      = u'Empresas'
     _order            = 'name'
     _sql_constraints  = {
         ('name_area',
          'UNIQUE(name)',
          u'A Empresa não pode ser repetida!'
         )
     }

     name              = fields.Char(
         string=u'Empresa',
     )
