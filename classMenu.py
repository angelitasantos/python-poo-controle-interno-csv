from time import sleep

from classValidacoes import *
from classInterface import *
from classArquivos import *
from classBackup import *

from classProdutos import *
from classClientes import *
from classFornecedores import *
from classVendas import *
from classCompras import *
from classContasReceber import *
from classContasPagar import *


lista_menu_principal = [
                        'Vendas',
                        'Compras',
                        'Produtos',
                        'Clientes',
                        'Fornececores',
                        'Contas a Receber',
                        'Contas a Pagar',
                        'Gerencial',
                        'Sair'
                        ]


lista_submenu = [
                        'Listar',
                        'Cadastrar',
                        'Pesquisar',
                        'Sair'
                        ]


class Menu:

    def __init__(self, menu):
        self.menu = menu


    def gerar_menu_principal(self):

        while True:
            resposta = Interface.apresentar_menu_principal(self, lista_menu_principal, 'MENU PRINCIPAL')

            if resposta == 1:
                Menu.conferir_arquivo_existe(self, arquivo_vendas, 1)
                Menu.gerar_menu_vendas(self, arquivo_vendas)

            elif resposta == 2:
                Menu.conferir_arquivo_existe(self, arquivo_compras, 2)
                Menu.gerar_menu_compras(self, arquivo_compras)

            elif resposta == 3:
                Menu.conferir_arquivo_existe(self, arquivo_produtos, 3)
                Menu.gerar_menu_produtos(self, arquivo_produtos)

            elif resposta == 4:
                Menu.conferir_arquivo_existe(self, arquivo_clientes, 4)
                Menu.gerar_menu_clientes(self, arquivo_clientes)

            elif resposta == 5:
                Menu.conferir_arquivo_existe(self, arquivo_fornecedores, 5)
                Menu.gerar_menu_fornecedores(self, arquivo_fornecedores)
                
            elif resposta == 6:
                Menu.conferir_arquivo_existe(self, arquivo_receber, 6)
                Menu.gerar_menu_contas_receber(self, arquivo_receber)

            elif resposta == 7:
                Menu.conferir_arquivo_existe(self, arquivo_pagar, 7)
                Menu.gerar_menu_contas_pagar(self, arquivo_pagar)

            elif resposta == 8:
                print('Gerencial')

            elif resposta == 9:
                print(f'{fontCor[1]}\nSaindo do Sistema ...\n')
                sleep(2)
                Interface.apresentar_cabecalho_interno(self, f'Até breve!', fontCor[1])
                break

            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def conferir_arquivo_existe(self, arquivo, opcao):
        if not Arquivo.analisar_arquivo_existe(self, arquivo):
            print(f'\n{fontCor[1]}Arquivo não existe.{fontCor[1]}')
            print(f'{fontCor[1]}Criando arquivo ...')
            sleep(2)
            Arquivo.criar_arquivo(self, arquivo, opcao)


    def gerar_menu_produtos(self, arquivo):

        while True:
            submenu = 'MENU PRODUTOS'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, submenu)

            if resposta == 1:
                sleep(1)
                Produtos.ler_arquivo_produtos(self, arquivo)
            elif resposta == 2:
                sleep(1)
                Produtos.cadastrar_produtos(self, arquivo)
            elif resposta == 3:
                sleep(1)
                Produtos.buscar_produto_descricao(self, arquivo)
            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break
            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_clientes(self, arquivo):

        while True:
            submenu = 'MENU PRODUTOS'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, submenu)

            if resposta == 1:
                sleep(1)
                Clientes.ler_arquivo_clientes(self, arquivo)
            elif resposta == 2:
                sleep(1)
                Clientes.cadastrar_clientes(self, arquivo)
            elif resposta == 3:
                sleep(1)
                Clientes.buscar_cliente(self, arquivo)
            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break
            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_fornecedores(self, arquivo):

        while True:
            submenu = 'MENU FORNECEDORES'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, submenu)
            if resposta == 1:
                sleep(1)
                Fornecedores.ler_arquivo_fornecedores(self, arquivo)
            elif resposta == 2:
                sleep(1)
                Fornecedores.cadastrar_fornecedores(self, arquivo)
            elif resposta == 3:
                sleep(1)
                Fornecedores.buscar_fornecedor(self, arquivo)
            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break
            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_vendas(self, arquivo):

        while True:
            submenu = 'MENU VENDAS'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, submenu)

            if resposta == 1:
                sleep(1)
                Vendas.ler_arquivo_vendas(self, arquivo)
            elif resposta == 2:
                sleep(1)
                Vendas.cadastrar_vendas(self, arquivo)
            elif resposta == 3:
                sleep(1)
                Vendas.buscar_vendas_cliente(self, arquivo)
            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break
            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_compras(self, arquivo):

        while True:
            submenu = 'MENU COMPRAS'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, submenu)

            if resposta == 1:
                sleep(1)
                Compras.ler_arquivo_compras(self, arquivo)
            elif resposta == 2:
                sleep(1)
                Compras.cadastrar_compras(self, arquivo)
            elif resposta == 3:
                sleep(1)
                Compras.buscar_compras_fornecedor(self, arquivo)
            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break
            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_contas_receber(self, arquivo):

        while True:
            submenu = 'MENU CONTAS A RECEBER'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, submenu)

            if resposta == 1:
                sleep(1)
                ContasReceber.ler_arquivo_contas_receber(self, arquivo)
            elif resposta == 2:
                sleep(1)
                ContasReceber.cadastrar_contas_receber(self, arquivo)
            elif resposta == 3:
                sleep(1)
                ContasReceber.buscar_contas_receber_cliente(self, arquivo)
            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break
            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_contas_pagar(self, arquivo):

        while True:
            submenu = 'MENU CONTAS A PAGAR'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, submenu)

            if resposta == 1:
                sleep(1)
                ContasPagar.ler_arquivo_contas_pagar(self, arquivo)
            elif resposta == 2:
                sleep(1)
                ContasPagar.cadastrar_contas_pagar(self, arquivo)
            elif resposta == 3:
                sleep(1)
                ContasPagar.buscar_contas_pagar_fornecedor(self, arquivo)
            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break
            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')

