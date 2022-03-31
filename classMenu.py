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


self = 'self'
lista_menu_principal = [
                        'Vendas',
                        'Compras',
                        'Produtos',
                        'Clientes',
                        'Fornececores',
                        'Contas a Receber',
                        'Contas a Pagar',
                        'Backup',
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
                if not Arquivo.analisar_arquivo_existe(self, arquivo_vendas):
                    print(f'\n{fontCor[1]}Arquivo não existe.{fontCor[1]}')
                    print(f'{fontCor[1]}Criando arquivo ...')
                    sleep(2)
                    Arquivo.criar_arquivo_vendas(self)
                    Menu.gerar_menu_vendas(self)
                else:
                    sleep(1)
                    Menu.gerar_menu_vendas(self)


            elif resposta == 2:
                if not Arquivo.analisar_arquivo_existe(self, arquivo_compras):
                    print(f'\n{fontCor[1]}Arquivo não existe.{fontCor[1]}')
                    print(f'{fontCor[1]}Criando arquivo ...')
                    sleep(2)
                    Arquivo.criar_arquivo_compras(self)
                    Menu.gerar_menu_compras(self)
                else:
                    sleep(1)
                    Menu.gerar_menu_compras(self)


            elif resposta == 3:
                if not Arquivo.analisar_arquivo_existe(self, arquivo_produtos):
                    print(f'\n{fontCor[1]}Arquivo não existe.{fontCor[1]}')
                    print(f'{fontCor[1]}Criando arquivo ...')
                    sleep(2)
                    Arquivo.criar_arquivo_produtos(self)
                    Menu.gerar_menu_produtos(self)
                else:
                    sleep(1)
                    Menu.gerar_menu_produtos(self)


            elif resposta == 4:
                if not Arquivo.analisar_arquivo_existe(self, arquivo_clientes):
                    print(f'\n{fontCor[1]}Arquivo não existe.{fontCor[1]}')
                    print(f'{fontCor[1]}Criando arquivo ...')
                    sleep(2)
                    Arquivo.criar_arquivo_clientes(self)
                    Menu.gerar_menu_clientes(self)
                else:
                    sleep(1)
                    Menu.gerar_menu_clientes(self)


            elif resposta == 5:
                if not Arquivo.analisar_arquivo_existe(self, arquivo_fornecedores):
                    print(f'\n{fontCor[1]}Arquivo não existe.{fontCor[1]}')
                    print(f'{fontCor[1]}Criando arquivo ...')
                    sleep(2)
                    Arquivo.criar_arquivo_fornecedores(self)
                    Menu.gerar_menu_fornecedores(self)
                else:
                    sleep(1)
                    Menu.gerar_menu_fornecedores(self)
                

            elif resposta == 6:
                if not Arquivo.analisar_arquivo_existe(self, arquivo_receber):
                    print(f'\n{fontCor[1]}Arquivo não existe.{fontCor[1]}')
                    print(f'{fontCor[1]}Criando arquivo ...')
                    sleep(2)
                    Arquivo.criar_arquivo_contas_receber(self)
                    Menu.gerar_menu_contas_receber(self)
                else:
                    sleep(1)
                    Menu.gerar_menu_contas_receber(self)


            elif resposta == 7:
                if not Arquivo.analisar_arquivo_existe(self, arquivo_pagar):
                    print(f'\n{fontCor[1]}Arquivo não existe.{fontCor[1]}')
                    print(f'{fontCor[1]}Criando arquivo ...')
                    sleep(2)
                    Arquivo.criar_arquivo_contas_pagar(self)
                    Menu.gerar_menu_contas_pagar(self)
                else:
                    sleep(1)
                    Menu.gerar_menu_contas_pagar(self)


            elif resposta == 8:
                print('Backup')


            elif resposta == 9:
                print(f'{fontCor[1]}\nSaindo do Sistema ...\n')
                sleep(2)
                Interface.apresentar_cabecalho_interno(self, f'Até breve!', fontCor[1])
                break


            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_produtos(self):

        while True:
            submenu = 'MENU PRODUTOS'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, submenu)

            if resposta == 1:
                sleep(1)
                Produtos.ler_arquivo_produtos(self, arquivo_produtos)


            elif resposta == 2:
                sleep(1)
                Produtos.cadastrar_produtos(self, arquivo_produtos)


            elif resposta == 3:
                sleep(1)
                lista = Produtos.buscar_produto_descricao(self, arquivo_produtos)
                '''
                if lista != None:
                    print()
                    print(f'{"id ":.<15} {lista[0]}')
                    print(f'{"descrição ":.<15} {lista[1]}')
                    print(f'{"categoria ":.<15} {lista[2]}')
                    preco = Validacoes.formatar_valor_real(float((lista[3])))
                    print(f'{"preço ":.<15} R$ {preco}')
                    print()
                '''

            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break


            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_clientes(self):

        while True:
            submenu = 'MENU PRODUTOS'
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, 'MENU CLIENTES')

            if resposta == 1:
                sleep(1)
                Clientes.ler_arquivo_clientes(self, arquivo_clientes)


            elif resposta == 2:
                sleep(1)
                Clientes.cadastrar_clientes(self, arquivo_clientes)


            elif resposta == 3:
                sleep(1)
                lista = Clientes.buscar_cliente(self, arquivo_clientes)
                if lista != None:
                    print()
                    print(f'{"id ":.<15} {lista[0]}')
                    print(f'{"nome ":.<15} {lista[1]}')
                    print(f'{"cidade ":.<15} {lista[2]}')
                    print(f'{"estado ":.<15} {lista[3]}')
                    print(f'{"canal venda ":.<15} {lista[4]}')
                    print()


            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break


            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_fornecedores(self):

        while True:
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, 'MENU FORNECEDORES')

            if resposta == 1:
                sleep(1)
                Fornecedores.ler_arquivo_fornecedores(self, arquivo_fornecedores)


            elif resposta == 2:
                sleep(1)
                Fornecedores.cadastrar_fornecedores(self, arquivo_fornecedores)


            elif resposta == 3:
                sleep(1)
                lista = Fornecedores.buscar_fornecedor(self, arquivo_fornecedores)
                if lista != None:
                    print()
                    print(f'{"id ":.<20} {lista[0]}')
                    print(f'{"nome ":.<20} {lista[1]}')
                    print(f'{"cidade ":.<20} {lista[2]}')
                    print(f'{"estado ":.<20} {lista[3]}')
                    print(f'{"tipo fornecedor ":.<20} {lista[4]}')
                    print()


            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break


            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_vendas(self):

        while True:
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, 'MENU VENDAS')

            if resposta == 1:
                sleep(1)
                Vendas.ler_arquivo_vendas(self, arquivo_vendas)


            elif resposta == 2:
                sleep(1)
                Vendas.cadastrar_vendas(self, arquivo_vendas)


            elif resposta == 3:
                sleep(1)
                lista = Vendas.buscar_vendas(self, arquivo_vendas)
                if lista != None:
                    print()
                    print(f'{"número ":.<15} {lista[0]}')
                    print(f'{"codigo ":.<15} {lista[1]}')
                    print(f'{"cliente ":.<15} {lista[2]}')
                    print(f'{"cidade ":.<15} {lista[3]}')
                    print(f'{"estado ":.<15} {lista[4]}')
                    print(f'{"canal venda ":.<15} {lista[5]}')
                    print(f'{"codigo ":.<15} {lista[6]}')
                    print(f'{"produto ":.<15} {lista[7]}')
                    print(f'{"categoria ":.<15} {lista[8]}')
                    print(f'{"qtde ":.<15} {lista[9]}')
                    preco = Validacoes.formatar_valor_real(float((lista[10])))
                    print(f'{"preco ":.<15} R$ {preco}')
                    valor_total = float(lista[9]) * float(lista[10])
                    total = Validacoes.formatar_valor_real(float((valor_total)))
                    print(f'{"total ":.<15} R$ {total}')
                    print()


            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break


            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_compras(self):

        while True:
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, 'MENU COMPRAS')

            if resposta == 1:
                sleep(1)
                Compras.ler_arquivo_compras(self, arquivo_compras)


            elif resposta == 2:
                sleep(1)
                Compras.cadastrar_compras(self, arquivo_compras)


            elif resposta == 3:
                sleep(1)
                lista = Compras.buscar_compras(self, arquivo_compras)
                if lista != None:
                    print()
                    print(f'{"número ":.<15} {lista[0]}')
                    print(f'{"codigo ":.<15} {lista[1]}')
                    print(f'{"fornecedor ":.<15} {lista[2]}')
                    print(f'{"cidade ":.<15} {lista[3]}')
                    print(f'{"estado ":.<15} {lista[4]}')
                    print(f'{"tipo forn ":.<15} {lista[5]}')
                    print(f'{"codigo ":.<15} {lista[6]}')
                    print(f'{"produto ":.<15} {lista[7]}')
                    print(f'{"categoria ":.<15} {lista[8]}')
                    print(f'{"qtde ":.<15} {lista[9]}')
                    preco = Validacoes.formatar_valor_real(float((lista[10])))
                    print(f'{"preco ":.<15} R$ {preco}')
                    valor_total = float(lista[9]) * float(lista[10])
                    total = Validacoes.formatar_valor_real(float((valor_total)))
                    print(f'{"total ":.<15} R$ {total}')
                    print()


            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break


            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_contas_receber(self):

        while True:
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, 'MENU CONTAS A RECEBER')

            if resposta == 1:
                sleep(1)
                ContasReceber.ler_arquivo_contas_receber(self, arquivo_receber)


            elif resposta == 2:
                sleep(1)
                ContasReceber.cadastrar_contas_receber(self, arquivo_receber)


            elif resposta == 3:
                sleep(1)
                lista = ContasReceber.buscar_contas_receber(self, arquivo_receber)
                if lista != None:
                    print()
                    print(f'{"número ":.<15} {lista[0]}')
                    print(f'{"codigo ":.<15} {lista[1]}')
                    print(f'{"cliente ":.<15} {lista[2]}')
                    print(f'{"cidade ":.<15} {lista[3]}')
                    print(f'{"estado ":.<15} {lista[4]}')
                    print(f'{"canal venda ":.<15} {lista[5]}')
                    print(f'{"parcela ":.<15} {lista[6]}')
                    valor = Validacoes.formatar_valor_real(float((lista[7])))
                    print(f'{"valor ":.<15} R$ {valor}')
                    print(f'{"vencimento ":.<15} {lista[8]}')
                    print(f'{"numero parcela ":.<15} {lista[9]}')
                    print(f'{"status ":.<15} {lista[10]}')
                    print()


            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break


            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')


    def gerar_menu_contas_pagar(self):

        while True:
            resposta = Interface.apresentar_menu_principal(self, lista_submenu, 'MENU CONTAS A PAGAR')

            if resposta == 1:
                sleep(1)
                ContasPagar.ler_arquivo_contas_pagar(self, arquivo_pagar)


            elif resposta == 2:
                sleep(1)
                ContasPagar.cadastrar_contas_pagar(self, arquivo_pagar)


            elif resposta == 3:
                sleep(1)
                lista = ContasPagar.buscar_contas_pagar(self, arquivo_pagar)
                if lista != None:
                    print()
                    print(f'{"número ":.<15} {lista[0]}')
                    print(f'{"codigo ":.<15} {lista[1]}')
                    print(f'{"fornecedor ":.<15} {lista[2]}')
                    print(f'{"cidade ":.<15} {lista[3]}')
                    print(f'{"estado ":.<15} {lista[4]}')
                    print(f'{"tipo forn ":.<15} {lista[5]}')
                    print(f'{"parcela ":.<15} {lista[6]}')
                    valor = Validacoes.formatar_valor_real(float((lista[7])))
                    print(f'{"valor ":.<15} R$ {valor}')
                    print(f'{"vencimento ":.<15} {lista[8]}')
                    print(f'{"numero parcela ":.<15} {lista[9]}')
                    print(f'{"status ":.<15} {lista[10]}')
                    print()


            elif resposta == 4:
                print(f'{fontCor[1]}\nVoltando ao menu principal ...\n{fontCor[0]}')
                sleep(2)
                break


            else:
                print(f'{bgCor[1]}ERRO: Por favor, digite uma opção válida!{bgCor[0]}')
