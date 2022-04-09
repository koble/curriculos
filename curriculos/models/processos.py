# -*- coding: utf-8 -*-

from odoo            import models, fields, api, exceptions, _
from datetime        import datetime, date
from odoo.exceptions import Warning as UserError

class processos(models.Model):
     _name             = 'curriculos.processos'
     _description      = u'Processos'
     _inherit          = ['mail.thread']
     _order            = 'data_inicio desc'

     name              = fields.Char(string=u'Processo',
                            # compute="_fill_processo",
                            # store=True,
                         )
     description       = fields.Text(string=u'Descrição')
     data_inicio       = fields.Date(string=u'Início',
        default=date.today().strftime('%Y-%m-%d'),
     )
     data_fim          = fields.Date(string=u'Conclusão')
     color             = fields.Integer(u'Cor')
     priority          = fields.Selection(
         [('0', 'Baixo'),
          ('1', 'Normal'),
          ('2', 'Alta')],
        u'Prioridade', default='1')
     cliente_id        = fields.Many2one('res.partner',
        string=u'Cliente',
        auto_join=True,
        domain=[('customer','=','True')],
     )
     state             = fields.Selection(
         [('running',u'Em Progresso'),('done',u'Concluído'),('cancelled',u'Cancelado')],
         string=u'Estágio',
         default='running',
         track_visibility='always',
     )
     area_funcional_id = fields.Many2one('curriculos.areas_funcionais',
         string=u'Área Funcional'
     )
     cargos_id         = fields.Many2one('curriculos.cargos',
         string=u'Cargo',
     )
     curriculos_ids    = fields.Many2many('curriculos.curriculos', 
         string=u'Currículos',
     )
     count_curriculos  = fields.Integer(u'Qtd',
         compute="_conta_curriculos",
         Store=True,
     )
     selecionado_id    = fields.Many2one('curriculos.curriculos',
         string=u'Selecionado',
     #    domain=[('id','in',curriculos_ids[0][2])],
     )

     @api.depends('curriculos_ids')
     @api.multi
     def _conta_curriculos(self):
         for s in self:
             s.count_curriculos = s.curriculos_ids and len(s.curriculos_ids) or 0

     @api.depends('cliente_id','cargos_id','data_inicio')
     def _fill_processo(self):
         try:
            if not self.cliente_id.name:
               nome = ''
            else:
               nome = self.cliente_id.name

            if not self.data_inicio:
               inicio = ''
            else:
               inicio    = datetime.strptime(self.data_inicio, '%Y-%m-%d').strftime('%b/%Y')

            if not self.cargos_id.name:
               cargo = ''
            else:
               cargo = self.cargos_id.name

            self.name = self.cliente_id.name + ' - ' + cargo + ' (' + inicio + ')'
         except:
            pass

     @api.onchange('area_funcional_id','cargos_id')
     def _domain_cargos_id(self):
         res           = {}
         res['domain'] = { 'cargos_id': [] }
         if self.cargos_id and self.area_funcional_id:
            if self.area_funcional_id != self.cargos_id.area_funcional_id:
               self.cargos_id = False
         elif not self.cargos_id and self.area_funcional_id:
            res['domain'] = { 'cargos_id': 
               [('area_funcional_id','=',self.area_funcional_id.id)] }
         elif self.cargos_id and not self.area_funcional_id:
            self.area_funcional_id = self.cargos_id.area_funcional_id
         return res

     @api.multi
     def concluir_processo(self):
         self.ensure_one()
         if not self.selecionado_id:
            raise UserError(_("Não pode concluir um processo sem um currículo selecionado!"))
         else:
            if not self.data_fim:
               data = fields.Date.today()
            else:
               data = self.data_fim
            self.write({
               'state'   : 'done',
               'data_fim': data,
            })

     @api.multi
     def reabrir_processo(self):
         self.ensure_one()
         self.write({
            'state'   : 'running',
         })

     @api.multi
     def cancelar_processo(self):
         self.ensure_one()
         if not self.data_fim:
            data = fields.Date.today()
         else:
            data = self.data_fim
         self.write({
            'state'   : 'cancelled',
            'data_fim': data,
         })
