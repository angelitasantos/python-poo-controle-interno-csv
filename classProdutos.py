from classValidacoes import *
from classInterface import *
from classArquivos import *
import csv


class Produtos:

    def __init__(self, arquivo, id, descricao, preco, categoria):
        self.arquivo = arquivo
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria


    def ler_arquivo_produtos(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            Interface.apresentar_cabecalho_interno(self, 'PRODUTOS CADASTRADOS')
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

            print(f'{bgCor[4]}{lista[0][0]:<14} {lista[0][1]:<45}{lista[0][2]:<25}{lista[0][3]:<15}{bgCor[0]}')
            print(Interface.incrementar_linha(self, tamanho, '~'))

            if len(lista) != 1:
                for linha in lista_ordenada:
                    preco = Validacoes.formatar_valor_real(float((linha[3])))
                    print(f'{linha[0]:>14} {linha[1]:<45}{linha[2]:<25}R$ {preco:.>11}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
            else:
                print(f'\n{fontCor[1]}Não existe nenhum produto cadastrado no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()


    def cadastrar_produtos(self, nome):
        try:
            arquivo = open(nome, 'a')
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgCor[0]}\n')
        else:
            try:
                escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
                Interface.apresentar_cabecalho_interno(self, 'CADASTRAR UM NOVO PRODUTO')

                id = int(Validacoes.gerar_id_sequencial(self, arquivo_produtos))
                print()

                desc = str(input(f'{"Digite a descrição ":.<25} ')).strip().upper()
                while Validacoes.validar_campo_vazio(self, desc):
                    desc = str(input(f'{"Digite a descrição ":.<25} ')).strip().upper()
                    if Validacoes.validar_tamanho_campo(self, len(desc), tamanho_25):
                        print(f'\n{fontCor[1]}O campo Descrição deve conter no máximo {tamanho_25} caracteres\n{fontCor[0]}')
                        desc = str(input(f'{"Digite a descrição ":.<25} ')).strip().upper()
                descricao = desc
                
                categoria = str(input(f'{"Digite a categoria ":.<25} ')).strip().upper()
                preco = Validacoes.digitar_numero_real(self)

                tabela = [id, descricao, categoria, preco]
                escritor.writerow(tabela)
            except:
                print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgCor[0]}\n')
            else:
                print(f'\n{bgCor[2]}Cadastro efetuado com sucesso.{bgCor[0]}\n')
                arquivo.close()


    def buscar_produto(self, nome):
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
                print(f'\n{fontCor[1]}Não existe nenhum produto cadastrado no sistema.\n{fontCor[0]}')
            elif len(tabela) != 1:
                codigo = str(input(f'\n{"Digite o código do produto":.<35} '))
                for linha in tabela: 
                    if linha[0] == codigo:
                        return [linha[0], linha[1], linha[2], linha[3]]
        finally:
            arquivo.close()


    def buscar_produto_descricao(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

            if len(lista) == 1:
                print(f'\n{fontCor[1]}Não existe nenhum produto cadastrado no sistema.\n{fontCor[0]}')
            elif len(lista) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR PRODUTO POR DESCRIÇÃO')

                descricao = str(input(f'\n{"Digite a descrição do produto":.<35} ')).strip().upper()
                palavra = descricao
                print(f'\n{bgCor[4]}{lista[0][0]:<14} {lista[0][1]:<45}{lista[0][2]:<25}{lista[0][3]:<15}{bgCor[0]}')
                print(Interface.incrementar_linha(self, tamanho, '~'))

                for linha in lista_ordenada: 
                    if palavra in linha[1] and linha[0] != 'ID':
                        preco = Validacoes.formatar_valor_real(float((linha[3])))
                        print(f'{linha[0]:>14} {linha[1]:<45}{linha[2]:<25}R$ {preco:.>11}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
        finally:
            arquivo.close()


    def buscar_produto_categoria(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

            if len(lista) == 1:
                print(f'\n{fontCor[1]}Não existe nenhum produto cadastrado no sistema.\n{fontCor[0]}')
            elif len(lista) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR PRODUTO POR CATEGORIA')

                descricao = str(input(f'\n{"Digite a categoria do produto":.<35} ')).strip().upper()
                palavra = descricao
                print(f'\n{bgCor[4]}{lista[0][0]:<14} {lista[0][1]:<45}{lista[0][2]:<25}{lista[0][3]:<15}{bgCor[0]}')
                print(Interface.incrementar_linha(self, tamanho, '~'))

                for linha in lista_ordenada:
                    if palavra in linha[2] and linha[0] != 'ID':
                        preco = Validacoes.formatar_valor_real(float((linha[3])))
                        print(f'{linha[0]:>14} {linha[1]:<45}{linha[2]:<25}R$ {preco:.>11}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
        finally:
            arquivo.close()


'''
self = 'self'
Produtos.ler_arquivo_produtos(self, arquivo_produtos)
busca = Produtos.buscar_produto(self, arquivo_produtos)
print(busca)
Produtos.buscar_produto_descricao(self, arquivo_produtos)
Produtos.cadastrar_produtos(self, arquivo_produtos)
Produtos.buscar_produto_categoria(self, arquivo_produtos)
'''
