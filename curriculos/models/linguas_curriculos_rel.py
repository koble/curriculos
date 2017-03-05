# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _

class linguas_curriculos_rel(models.Model):
     _name             = 'curriculos.linguas_curriculos_rel'
     _description      = u'Línguas e Currículos'
     _order            = 'name'
     _sql_constraints  = [
         ('rel_unique', 
          'UNIQUE(curriculos_ids, linguas_ids)', 
          u'Língua já cadastrada neste currículo !'
         )
     ]
     _order            = 'curriculos_ids,linguas_ids'

     proficiencia      = fields.Selection(
         string=u'Proficiência',
         selection=[
                    ('basico',u'Básico'),
                    ('intermediario',u'Intermediário'),
                    ('avancado',u'Avançado'),
                    ('fluente',u'Fluente'),
                   ],
     )
     curriculos_ids    = fields.Many2one('curriculos.curriculos',
         string=u'Currículos',
     )
     linguas_ids       = fields.Many2one('curriculos.linguas',
         string=u'Línguas',
     )

