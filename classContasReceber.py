from classValidacoes import *
from classInterface import *
from classArquivos import *
from classVendas import *
import csv  # - CSV -> Comma Separated Values


class ContasReceber:

    def __init__(self, arquivo, venda, parcela, valor, vencimento):
        self.arquivo = arquivo
        self.venda = venda
        self.parcela = parcela
        self.valor = valor
        self.vencimento = vencimento


    def ler_arquivo_contas_receber(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            Interface.apresentar_cabecalho_interno(self, 'CONTAS A RECEBER')
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            tabela = []

            for linha in leitor:
                tabela.append(linha)

            print(f'{bgCor[4]}{tabela[0][0]:<15}{tabela[0][2]:<35}{tabela[0][6]:<10}{tabela[0][7]:<15}{tabela[0][8]:<11}{tabela[0][10]:<14}{bgCor[0]}')
            print(Interface.incrementar_linha(self, tamanho, '~'))

            if len(tabela) != 1:
                for linha in tabela[1:]:
                    valor = Validacoes.formatar_valor_real(float((linha[7])))
                    print(f'{linha[0]:<15}{linha[2]:<35}{linha[6]:<9} R$ {valor:.>11} {linha[8]:<11}{linha[10]:<14}')
                print(Interface.incrementar_linha(self, tamanho, '~'))
            else:
                print(f'\n{fontCor[1]}Não existe nenhum parcela registrada no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()


    def cadastrar_contas_receber(self, nome):
        try:
            arquivo = open(nome, 'a')
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgCor[0]}\n')
        else:
            try:
                escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
                Interface.apresentar_cabecalho_interno(self, 'CADASTRAR UMA NOVA PARCELA')

                print()
                lista_vendas = Vendas.buscar_vendas(self, arquivo_vendas)
                if lista_vendas != None:
                    numero = lista_vendas[0]
                    cod_cliente = lista_vendas[1]
                    nome_cliente = lista_vendas[2]
                    cidade_cliente = lista_vendas[3]
                    estado_cliente = lista_vendas[4]
                    canal_venda_cliente = lista_vendas[5]
                    print(f'{numero}-{nome_cliente}-{cidade_cliente}/{estado_cliente}')
                    
                parcela = int(input(f'{"Digite a parcela ":.<25} '))
                valor = float(input(f'{"Digite o valor ":.<25} '))
                vencimento = str(input(f'{"Digite o vencimento ":.<25} '))
                numparc = f'{numero}-{parcela}'
                status = 'EM ABERTO'

                contas_receber = [  numero, cod_cliente, nome_cliente, cidade_cliente, estado_cliente, canal_venda_cliente,
                                    parcela, valor, vencimento, numparc, status]
                escritor.writerow(contas_receber)
            except:
                print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgCor[0]}\n')
            else:
                print(f'\n{bgCor[2]}Parcela registrada com sucesso.{bgCor[0]}\n')
                arquivo.close()


    def buscar_contas_receber(self, nome):
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
                print(f'\n{fontCor[1]}Não existe nenhum parcela registrada no sistema.\n{fontCor[0]}')
            elif len(tabela) != 1:
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR CONTAS A RECEBER')
                numero_parcela = str(input(f'{"Digite o número ":.<25} '))
                for linha in tabela: 
                    if linha[9] == numero_parcela:
                        return [linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9],linha[10]]
                else:
                    print(f'\n{fontCor[1]}Não existe nenhum parcela registrada no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()
