from classValidacoes import *
from classInterface import *
from classArquivos import *
from classProdutos import *
from classClientes import *
import csv


class Vendas:

    def __init__(self, arquivo, numero, cliente, produto, qtde):
        self.arquivo = arquivo
        self.numero = numero
        self.cliente = cliente
        self.produto = produto
        self.qtde = qtde


    def ler_arquivo_vendas(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            Interface.apresentar_cabecalho_interno(self, 'PEDIDOS DE VENDA')
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

            print(f'{bgCor[4]}{tabela[0][0]:<15}{tabela[0][2]:<30}{tabela[0][7]:<30}{tabela[0][9]:<10}{tabela[0][10]:<15}{bgCor[0]}')
            print(Interface.incrementar_linha(self, tamanho, '~'))

            if len(tabela) != 1:
                for linha in tabela[1:]:
                    qtde = Validacoes.formatar_quantidade(float((linha[9])))
                    total = float((linha[9])) * float((linha[10]))
                    valor = Validacoes.formatar_valor_real(total)
                    print(f'{linha[0]:<15}{linha[2]:<30}{linha[7]:<30}{qtde:>9} R$ {valor:.>11}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
            else:
                print(f'\n{fontCor[1]}Não existe nenhum venda registrada no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()


    def cadastrar_vendas(self, nome):
        try:
            arquivo = open(nome, 'a')
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgCor[0]}\n')
        else:
            try:
                escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
                Interface.apresentar_cabecalho_interno(self, 'CADASTRAR UMA NOVA VENDA')

                numero = int(Validacoes.gerar_id_sequencial(self, arquivo_vendas))
                print()

                lista_clientes = Clientes.buscar_cliente(self, arquivo_clientes)
                if lista_clientes != None:
                    cod_cliente = lista_clientes[0]
                    nome_cliente = lista_clientes[1]
                    cidade_cliente = lista_clientes[2]
                    estado_cliente = lista_clientes[3]
                    canal_venda_cliente = lista_clientes[4]
                    print(f'{nome_cliente}-{cidade_cliente}/{estado_cliente}')

                resposta = str(input(f'\nQuer consultar o código do produto? [S/N] '))
                if resposta == 'S' or resposta == 's':
                    Produtos.buscar_produto_descricao(self, arquivo_produtos)      

                busca_produto = Produtos.buscar_produto(self, arquivo_produtos)

                while busca_produto == None:
                    print(f'\n{fontCor[1]}Você não digitou um código válido.{fontCor[0]}')
                    busca_produto = Produtos.buscar_produto(self, arquivo_produtos)

                if busca_produto != None:
                    cod_produto = busca_produto[0]
                    nome_produto = busca_produto[1]
                    categoria_produto = busca_produto[2]
                    qtde = Validacoes.validar_numero_real(self, f'{"Digite a quantidade ":.<25} ')
                    preco_produto = busca_produto[3]
                    preco = Validacoes.formatar_valor_real(float((busca_produto[3])))
                    print(f'{nome_produto}-{categoria_produto} Preço unitário: R$ {preco}')

                tabela = [
                    numero, cod_cliente, nome_cliente, cidade_cliente, estado_cliente, canal_venda_cliente,
                    cod_produto, nome_produto, categoria_produto, qtde, preco_produto]

                escritor.writerow(tabela)
            except:
                print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgCor[0]}\n')
            else:
                print(f'\n{bgCor[2]}Venda registrada com sucesso.{bgCor[0]}\n')
                arquivo.close()


    def buscar_vendas(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            tabela = []

            for linha in leitor:
                tabela.append(linha)

            if len(tabela) == 1:
                print(f'\n{fontCor[1]}Não existe nenhum venda registrada no sistema.\n{fontCor[0]}')
            elif len(tabela) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR VENDA')
                numero_venda = str(input(f'{"Digite o número ":.<25} '))
                for linha in tabela: 
                    if linha[0] == numero_venda:
                        return [linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10]]
                else:
                    print(f'\n{fontCor[1]}Não existe nenhum venda registrada no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()
