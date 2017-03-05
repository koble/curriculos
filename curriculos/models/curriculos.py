# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions, _

class curriculos(models.Model):
     _name             = 'curriculos.curriculos'
     _description      = u'Currículos'
     _inherit          = ['mail.thread']
     _order            = 'name'

     name              = fields.Char(
         string=u'Nome',
     )
     email             = fields.Char(u'Email')
     endereco          = fields.Text(u'Endereço')
     telefone          = fields.Char(u'Telefone')
     celular           = fields.Char(u'Celular')
     profissoes_id     = fields.Many2one('curriculos.profissoes',
         string=u'Profissão',
     )
     analise           = fields.Text()
     processos_ids     = fields.Many2many('curriculos.processos', 
         string=u'Processos Seletivos',
     )
     attachment_ids    = fields.Many2many(
         comodel_name='ir.attachment',
         relation='curriculos_curriculos_attachment_rel',
         column1='curriculos_id',
         column2='attachment_id',
         ondelete='cascade',
         string=u'Anexo',
     )
     curriculos_linguas_rel_ids   = fields.One2many(
         'curriculos.linguas_curriculos_rel',
         'curriculos_ids',
         ondelete='cascade',
     )
     experiencias_ids             = fields.One2many(
         'curriculos.experiencias',
         'curriculos_ids',
         ondelete='cascade',
     )
