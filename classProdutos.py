from classValidacoes import *
from classInterface import *
from classArquivos import *
import csv  # - CSV -> Comma Separated Values


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
            tabela = []

            for linha in leitor:
                tabela.append(linha)

            print(f'{bgCor[4]}{tabela[0][0]:<15}{tabela[0][1]:<45}{tabela[0][2]:<25}{tabela[0][3]:<15}{bgCor[0]}')
            print(Interface.incrementar_linha(self, tamanho, '~'))

            if len(tabela) != 1:
                for linha in tabela[1:]:
                    preco = Validacoes.formatar_valor_real(float((linha[3])))
                    print(f'{linha[0]:<15}{linha[1]:<45}{linha[2]:<25}R$ {preco:.>11}')
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

                # validar se já existe o identificador gerado
                id = str(Validacoes.gerar_identificador(self))
                print()
                descricao = str(input(f'{"Digite a descrição ":.<25} ')).strip().upper()
                categoria = str(input(f'{"Digite a categoria ":.<25} ')).strip().upper()
                preco = Validacoes.validar_numero_real(self, f'{"Digite o preço ":.<25} ')

                clientes = [id, descricao, categoria, preco]
                escritor.writerow(clientes)
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
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR PRODUTO')
                codigo_produto = str(input(f'{"Digite o produto ":.<25} '))
                for linha in tabela: 
                    if linha[0] == codigo_produto:
                        return [linha[0], linha[1], linha[2], linha[3]]
                else:
                    print(f'\n{fontCor[1]}Não existe nenhum produto cadastrado no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()
