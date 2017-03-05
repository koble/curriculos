# -*- coding: utf-8 -*-
{
    'name': "Controle de Currículos",

    'summary': """
        Implementar um controle de currículos internos e processos seletivos.
        """,

    'description': """
       Cria as seguintes funções:
        - Controle de Currículos
        - Processos Seletivos
        - Áreas Funcionais
        """,

    'author': "Koble Open Solutions",
    'website': "http://www.koble.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Recruitment',
    'version': '0.1',
#    'license': 'LGPL',
    'website': 'https://github.com/koble/orchestrator',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/curriculos_security.xml',
        'security/ir.model.access.csv',
        'views/menu_principal.xml',
        'views/curriculos.xml',
        'views/experiencias.xml',
        'views/processos.xml',
        'views/areas_funcionais.xml',
        'views/cargos.xml',
        'views/clientes.xml',
        'views/linguas.xml',
        'views/empresas.xml',
        'views/profissoes.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
