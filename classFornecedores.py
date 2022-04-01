from classValidacoes import *
from classInterface import *
from classArquivos import *
import csv


class Fornecedores:

    def __init__(self, arquivo, id, nome_fornecedor, cidade, estado, tipoforn):
        self.arquivo = arquivo
        self.id = id
        self.nome_fornecedor = nome_fornecedor
        self.cidade = cidade
        self.estado = estado
        self.tipoforn = tipoforn


    def ler_arquivo_fornecedores(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            Interface.apresentar_cabecalho_interno(self, 'FORNECEDORES CADASTRADOS')
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

            print(f'{bgCor[4]}{lista[0][0]:<14} {lista[0][1]:<35}{lista[0][2]:<30}{lista[0][3]:<5}{lista[0][4]:<15}{bgCor[0]}')
            print(Interface.incrementar_linha(self, tamanho, '~'))

            if len(lista) != 1:
                for linha in lista_ordenada:
                    print(f'{linha[0]:>14} {linha[1]:<35}{linha[2]:<30}{linha[3]:<5}{linha[4]:<15}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
            else:
                print(f'\n{fontCor[1]}Não existe nenhum fornecedor cadastrado no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()


    def cadastrar_fornecedores(self, nome):
        try:
            arquivo = open(nome, 'a')
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgCor[0]}\n')
        else:
            try:
                escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
                Interface.apresentar_cabecalho_interno(self, 'CADASTRAR UM NOVO FORNECEDOR')

                id = int(Validacoes.gerar_id_sequencial(self, arquivo_fornecedores))
                print()

                nome_for = str(input(f'{"Digite o nome ":.<25} ')).strip().upper()
                while Validacoes.validar_campo_vazio(self, nome_for):
                    nome_for = str(input(f'{"Digite o nome ":.<25} ')).strip().upper()
                    if Validacoes.validar_tamanho_campo(self, len(nome_for), tamanho_25):
                        print(f'\n{fontCor[1]}O campo Nome deve conter no máximo {tamanho_25} caracteres\n{fontCor[0]}')
                        nome_for = str(input(f'{"Digite o nome ":.<25} ')).strip().upper()
                nome_fornecedor = nome_for

                cidade = str(input(f'{"Digite a cidade ":.<25} ')).strip().upper()
                estado = str(input(f'{"Digite o estado ":.<25} ')).strip().upper()
                tipoforn = str(input(f'{"Digite o tipo de fornecedor ":.<25} ')).strip().upper()

                tabela = [id, nome_fornecedor, cidade, estado, tipoforn]
                escritor.writerow(tabela)
            except:
                print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgCor[0]}\n')
            else:
                print(f'\n{bgCor[2]}Cadastro efetuado com sucesso.{bgCor[0]}\n')
                arquivo.close()


    def buscar_fornecedor(self, nome):
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
                print(f'\n{fontCor[1]}Não existe nenhum fornecedor cadastrado no sistema.\n{fontCor[0]}')
            elif len(tabela) != 1:
                codigo = str(input(f'\n{"Digite o código do fornecedor ":.<35} '))
                for linha in tabela: 
                    if linha[0] == codigo:
                        return [linha[0], linha[1], linha[2], linha[3], linha[4]]
        finally:
            arquivo.close()


    def buscar_fornecedor_nome(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

            if len(lista) == 1:
                print(f'\n{fontCor[1]}Não existe nenhum fornecedor cadastrado no sistema.\n{fontCor[0]}')
            elif len(lista) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR FORNECEDOR PELO NOME')

                descricao = str(input(f'\n{"Digite o nome do fornecedor":.<35} ')).strip().upper()
                palavra = descricao
                print(f'\n{bgCor[4]}{lista[0][0]:<14} {lista[0][1]:<35}{lista[0][2]:<30}{lista[0][3]:<5}{lista[0][4]:<15}{bgCor[0]}')
                print(Interface.incrementar_linha(self, tamanho, '~'))

                for linha in lista_ordenada: 
                    if palavra in linha[1] and linha[0] != 'ID':
                        print(f'{linha[0]:>14} {linha[1]:<35}{linha[2]:<30}{linha[3]:<5}{linha[4]:<15}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
        finally:
            arquivo.close()


    def buscar_fornecedor_tipo(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

            if len(lista) == 1:
                print(f'\n{fontCor[1]}Não existe nenhum fornecedor cadastrado no sistema.\n{fontCor[0]}')
            elif len(lista) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR FORNECEDOR POR TIPO')

                descricao = str(input(f'\n{"Digite o tipo de fornecedor ":.<35} ')).strip().upper()
                palavra = descricao
                print(f'\n{bgCor[4]}{lista[0][0]:<14} {lista[0][1]:<35}{lista[0][2]:<30}{lista[0][3]:<5}{lista[0][4]:<15}{bgCor[0]}')
                print(Interface.incrementar_linha(self, tamanho, '~'))

                for linha in lista_ordenada: 
                    if palavra in linha[4] and linha[0] != 'ID':
                        print(f'{linha[0]:>14} {linha[1]:<35}{linha[2]:<30}{linha[3]:<5}{linha[4]:<15}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
        finally:
            arquivo.close()


'''
self = 'self'
Fornecedores.ler_arquivo_fornecedores(self, arquivo_fornecedores)
busca = Fornecedores.buscar_fornecedor(self, arquivo_fornecedores)
print(busca)
Fornecedores.buscar_fornecedor_nome(self, arquivo_fornecedores)
Fornecedores.cadastrar_fornecedores(self, arquivo_fornecedores)
Fornecedores.buscar_fornecedor_tipo(self, arquivo_fornecedores)
'''
