from classValidacoes import *
from classInterface import *
from classArquivos import *
import csv  # - CSV -> Comma Separated Values


class Clientes:

    def __init__(self, arquivo, id, nome_cliente, cidade, estado, canalvenda):
        self.arquivo = arquivo
        self.id = id
        self.nome_cliente = nome_cliente
        self.cidade = cidade
        self.estado = estado
        self.canalvenda = canalvenda


    def ler_arquivo_clientes(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            Interface.apresentar_cabecalho_interno(self, 'CLIENTES CADASTRADOS')
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            tabela = []

            for linha in leitor:
                tabela.append(linha)

            print(f'{bgCor[4]}{tabela[0][0]:<15}{tabela[0][1]:<35}{tabela[0][2]:<30}{tabela[0][3]:<5}{tabela[0][4]:<15}{bgCor[0]}')
            print(Interface.incrementar_linha(self, tamanho, '~'))

            if len(tabela) != 1:
                for linha in tabela[1:]:
                    print(f'{linha[0]:<15}{linha[1]:<35}{linha[2]:<30}{linha[3]:<5}{linha[4]:<15}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
            else:
                print(f'\n{fontCor[1]}Não existe nenhum cliente cadastrado no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()


    def cadastrar_clientes(self, nome):
        try:
            arquivo = open(nome, 'a')
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgCor[0]}\n')
        else:
            try:
                escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
                Interface.apresentar_cabecalho_interno(self, 'CADASTRAR UM NOVO CLIENTE')

                # validar se já existe o identificador gerado
                id = str(Validacoes.gerar_identificador(self))
                print()
                nome_cliente = str(input(f'{"Digite o nome ":.<25} ')).strip().upper()
                cidade = str(input(f'{"Digite a cidade ":.<25} ')).strip().upper()
                estado = str(input(f'{"Digite o estado ":.<25} ')).strip().upper()
                canalvenda = str(input(f'{"Digite o canal venda ":.<25} ')).strip().upper()

                produtos = [id, nome_cliente, cidade, estado, canalvenda]
                escritor.writerow(produtos)
            except:
                print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgCor[0]}\n')
            else:
                print(f'\n{bgCor[2]}Cadastro efetuado com sucesso.{bgCor[0]}\n')
                arquivo.close()


    def buscar_cliente(self, nome):
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
                print(f'\n{fontCor[1]}Não existe nenhum cliente cadastrado no sistema.\n{fontCor[0]}')
            elif len(tabela) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR CLIENTE')
                codigo_cliente = str(input(f'{"Digite o cliente ":.<25} '))
                for linha in tabela: 
                    if linha[0] == codigo_cliente:
                        return [linha[0], linha[1], linha[2], linha[3], linha[4]]
                else:
                    print(f'\n{fontCor[1]}Não existe nenhum cliente cadastrado no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()
