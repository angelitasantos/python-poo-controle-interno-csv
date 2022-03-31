from classValidacoes import *
from classInterface import *
from classArquivos import *
from classCompras import *
import csv  # - CSV -> Comma Separated Values


class ContasPagar:

    def __init__(self, arquivo, compra, parcela, valor, vencimento):
        self.arquivo = arquivo
        self.compra = compra
        self.parcela = parcela
        self.valor = valor
        self.vencimento = vencimento


    def ler_arquivo_contas_pagar(self, nome):
        try:
            arquivo = open(nome, 'r')
        except:
            print(f'\n{bgCor[1]}ERRO! Confira se o arquivo existe.{bgCor[0]}\n')
        else:
            Interface.apresentar_cabecalho_interno(self, 'CONTAS A PAGAR')
            leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
            
            lista = list(leitor)
            lista_ordenada = sorted (lista[1:], key = lambda dado: str(dado[1]))

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


    def cadastrar_contas_pagar(self, nome):
        try:
            arquivo = open(nome, 'a')
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgCor[0]}\n')
        else:
            try:
                escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
                Interface.apresentar_cabecalho_interno(self, 'CADASTRAR UMA NOVA PARCELA')

                print()
                lista_compras = Compras.buscar_compras(self, arquivo_compras)
                if lista_compras != None:
                    numero = lista_compras[0]
                    cod_fornecedor = lista_compras[1]
                    nome_fornecedor = lista_compras[2]
                    cidade_fornecedor = lista_compras[3]
                    estado_fornecedor = lista_compras[4]
                    tipo_fornecedor = lista_compras[5]
                    print(f'{numero}-{nome_fornecedor}-{cidade_fornecedor}/{estado_fornecedor}')
                    
                parcela = int(input(f'{"Digite a parcela ":.<25} '))
                valor = float(input(f'{"Digite o valor ":.<25} '))
                vencimento = str(input(f'{"Digite o vencimento ":.<25} '))
                numparc = f'{numero}-{parcela}'
                status = 'EM ABERTO'

                contas_receber = [  numero, cod_fornecedor, nome_fornecedor, cidade_fornecedor, estado_fornecedor, tipo_fornecedor,
                                    parcela, valor, vencimento, numparc, status]
                escritor.writerow(contas_receber)
            except:
                print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgCor[0]}\n')
            else:
                print(f'\n{bgCor[2]}Parcela registrada com sucesso.{bgCor[0]}\n')
                arquivo.close()


    def buscar_contas_pagar(self, nome):
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
                Interface.apresentar_cabecalho_interno(self, 'PESQUISAR CONTAS A PAGAR')
                numero_parcela = str(input(f'{"Digite o número ":.<25} '))
                for linha in tabela: 
                    if linha[9] == numero_parcela:
                        return [linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9],linha[10]]
                else:
                    print(f'\n{fontCor[1]}Não existe nenhum parcela registrada no sistema.\n{fontCor[0]}')
        finally:
            arquivo.close()