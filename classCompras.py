from classValidacoes import *
from classInterface import *
from classArquivos import *
from classProdutos import *
from classFornecedores import *
import csv  # - CSV -> Comma Separated Values


class Compras:

    def __init__(self, arquivo, numero, fornecedor, produto, qtde, preco):
        self.arquivo = arquivo
        self.numero = numero
        self.fornecedor = fornecedor
        self.produto = produto
        self.qtde = qtde
        self.preco = preco


    def ler_arquivo_compras(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            Interface.apresentar_cabecalho_interno(self, 'PEDIDOS DE COMPRA')
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            tabela = []

            for linha in leitor:
                tabela.append(linha)

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
                print(f'\n{fontCor[1]}Não existe nenhum compra registrada no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()


    def cadastrar_compras(self, nome):
        try:
            arquivo = open(nome, 'a')
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgCor[0]}\n')
        else:
            try:
                escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
                Interface.apresentar_cabecalho_interno(self, 'CADASTRAR UMA NOVA COMPRA')

                # validar se já existe o identificador gerado
                numero = str(Validacoes.gerar_identificador(self))

                print()
                lista_fornecedores = Fornecedores.buscar_fornecedor(self, arquivo_fornecedores)
                if lista_fornecedores != None:
                    cod_fornecedor = lista_fornecedores[0]
                    nome_fornecedor = lista_fornecedores[1]
                    cidade_fornecedor = lista_fornecedores[2]
                    estado_fornecedor = lista_fornecedores[3]
                    tipo_fornecedor = lista_fornecedores[4]
                    print(f'{nome_fornecedor}-{cidade_fornecedor}/{estado_fornecedor}')

                lista_produtos = Produtos.buscar_produto(self, arquivo_produtos)
                if lista_produtos != None:
                    cod_produto = lista_produtos[0]
                    nome_produto = lista_produtos[1]
                    categoria_produto = lista_produtos[2]
                    qtde = Validacoes.validar_numero_real(self, f'{"Digite a quantidade ":.<25} ')
                    preco_produto = Validacoes.validar_numero_real(self, f'{"Digite o preço ":.<25} ')
                    preco = Validacoes.formatar_valor_real(float((preco_produto)))
                    print(f'{nome_produto}-{categoria_produto} Preço unitário: R$ {preco}')

                compras = [
                    numero, cod_fornecedor, nome_fornecedor, cidade_fornecedor, estado_fornecedor, tipo_fornecedor,
                    cod_produto, nome_produto, categoria_produto, qtde, preco_produto]

                escritor.writerow(compras)
            except:
                print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgCor[0]}\n')
            else:
                print(f'\n{bgCor[2]}Cadastro efetuado com sucesso.{bgCor[0]}\n')
                arquivo.close()


    def buscar_compras(self, nome):
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
                print(f'\n{fontCor[1]}Não existe nenhum compra registrada no sistema.\n{fontCor[0]}')
            elif len(tabela) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR COMPRA')
                numero_compra = str(input(f'{"Digite o número ":.<25} '))
                for linha in tabela: 
                    if linha[0] == numero_compra:
                        return [linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10]]
                else:
                    print(f'\n{fontCor[1]}Não existe nenhum compra registrada no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()
