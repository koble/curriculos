# -*- coding: utf-8 -*-

from odoo       import models, fields, api, exceptions
import textract
import tempfile
import base64


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
     # bairro            = fields.Char(u'Bairro')
     # cidade            = fields.Char(u'Cidade')
     # cep               = fields.Char(u'CEP')
     # estado            = fields.Char(u'Estado')
     telefone          = fields.Char(u'Telefone')
     celular           = fields.Char(u'Celular')
     profissoes_id     = fields.Many2one('curriculos.profissoes',
         string=u'Profissão',
     )
     cargo_atual_id    = fields.Many2one('curriculos.cargos',
         string=u'Cargo Atual',
     )
     cargo_anterior_id = fields.Many2one('curriculos.cargos',
         string=u'Cargo Anterior',
     )
     analise           = fields.Text()
     processos_ids     = fields.Many2many('curriculos.processos', 
         string=u'Processos Seletivos',
     )
     anexo = fields.Binary(
         string='Currículo Anexo',
     )
     nome_anexo = fields.Char(
         string='Currículo Anexo',
     )
     conteudo_indexado = fields.Text(
         string='Conteúdo Indexado',
         compute='_compute_conteudo_indexado',
         store=True,
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

     @api.depends('anexo')
     def _compute_conteudo_indexado(self):
         for curriculo in self:
             conteudo_indexado = False
             if curriculo.anexo:
                 arquivo = tempfile.NamedTemporaryFile()
                 arquivo.seek(0)
                 arquivo.write(base64.b64decode(curriculo.anexo))
                 arquivo.flush()
                 conteudo_indexado = textract.process(arquivo.name)
             curriculo.conteudo_indexado = conteudo_indexado

     def compute_conteudo_indexado(self):
         self.ensure_one()
         self._compute_conteudo_indexado()
