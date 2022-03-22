from classValidacoes import *
from classInterface import *
from classArquivos import *
from classMenu import *
from classBackup import *

from classProdutos import *
from classClientes import *
from classFornecedores import *
from classVendas import *
from classCompras import *
from classContasReceber import *
from classContasPagar import *


self = 'self'
print()
nome_app = 'CONTROLE DE VENDAS E COMPRAS'
Interface.apresentar_cabecalho_sistema(self, nome_app)
Menu.gerar_menu_principal(self)
