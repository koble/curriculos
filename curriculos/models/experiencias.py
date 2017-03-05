# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _
from datetime   import datetime

class experiencias(models.Model):
     _name             = 'curriculos.experiencias'
     _description      = u'Experiências Profissionais'
     _order            = 'name'

     name        = fields.Char(string=u'Experiência',
                               compute="_fill_name", 
                               store=True,
                              )

     empresas_id = fields.Many2one(
         'curriculos.empresas',
         string=u'Empresa',
     )
     cargos_id    = fields.Many2one(
         'curriculos.cargos',
         string=u'Cargo',
     )
     inicio       = fields.Date(string=u'Início')
     fim          = fields.Date(string=u'Fim')
     experiencia  = fields.Text(string=u'Experiência')
     curriculos_ids = fields.Many2one('curriculos.curriculos',
                                      ondelete='restrict')

     @api.depends('empresas_id', 'inicio', 'fim')
     def _fill_name(self):
         try:
            if not self.empresas_id.name:
               nome = ''
            else:
               nome = self.empresas_id.name

            if not self.inicio:
               inicio = ''
            else:
               inicio = datetime.strptime(self.inicio, '%Y-%m-%d').strftime('%b/%Y')

            if not self.fim:
               fim = ''
            else:
               fim    = datetime.strptime(self.fim   , '%Y-%m-%d').strftime('%b/%Y') or ''

            self.name = self.empresas_id.name + ' (' + inicio + '-' + fim + ')'
         except:
            pass
