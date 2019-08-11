# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _

class areas_funcionais(models.Model):
     _name             = 'curriculos.areas_funcionais'
     _description      = u'Areas Funcionais'

     name              = fields.Char(
         string=u'Área Funcional',
     )
     description       = fields.Text(
         string=u'Descrição',
     )
     curriculos_ids    = fields.Many2many('curriculos.curriculos',
         string=u'Curriculos',
         ondelete='restrict',
     )
     processos_ids     = fields.Many2many('curriculos.processos', 
         string=u'Processos Seletivos',
         ondelete='restrict',
     )
     cargos_ids        = fields.One2many(
         'curriculos.cargos',
         'area_funcional_id',
         string=u'Cargos',
         ondelete='restrict',
     )
