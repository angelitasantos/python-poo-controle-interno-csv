from classValidacoes import *
from classInterface import *
import csv


arquivo_produtos = 'tbprodutos.csv'
arquivo_clientes = 'tbclientes.csv'
arquivo_fornecedores = 'tbfornecedores.csv'
arquivo_vendas = 'tbvendas.csv'
arquivo_compras = 'tbcompras.csv'
arquivo_receber = 'tbreceber.csv'
arquivo_pagar = 'tbpagar.csv'


class Arquivo:

    def __init__(self, arquivo):
        self.arquivo = arquivo


    def analisar_arquivo_existe(self, arquivo_csv):
        try:
            arquivo = open(arquivo_csv, 'r')
            arquivo.close()
        except FileNotFoundError:
            return False
        else:
            return True


    def criar_arquivo(self, arquivo_csv):
        try:
            arquivo = open(arquivo_csv, 'w')
            arquivo.close()
        except:
            print(f'\n{bgCor[1]}ERRO! Ocorreu um erro ao criar o arquivo.{bgCor[0]}\n')
        else:
            print(f'{bgCor[2]}Arquivo criado com sucesso: {arquivo_csv}{bgCor[0]}\n')


    def criar_arquivo_produtos(self):
        arquivo = arquivo_produtos
        Arquivo.criar_arquivo(self, arquivo)

        arquivo = open(arquivo, 'a')
        escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')

        id = 'ID'
        produto = 'DESCRIÇÃO'
        categoria = 'CATEGORIA'
        preco = 'PREÇO'

        tabela = [id, produto, categoria, preco]
        escritor.writerow(tabela)
        

    def criar_arquivo_clientes(self):
        arquivo = 'tbclientes.csv'
        Arquivo.criar_arquivo(self, arquivo)

        arquivo = open(arquivo, 'a')
        escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')

        id = 'ID'
        cliente = 'CLIENTE'
        cidade = 'CIDADE'
        estado = 'UF'
        canalvenda = 'CANAL VENDA'

        tabela = [id, cliente, cidade, estado, canalvenda]
        escritor.writerow(tabela)


    def criar_arquivo_fornecedores(self):
        arquivo = 'tbfornecedores.csv'
        Arquivo.criar_arquivo(self, arquivo)

        arquivo = open(arquivo, 'a')
        escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')

        id = 'ID'
        fornecedor = 'FORNECEDOR'
        cidade = 'CIDADE'
        estado = 'UF'
        tipoforn = 'TIPO FORN'

        tabela = [id, fornecedor, cidade, estado, tipoforn]
        escritor.writerow(tabela)


    def criar_arquivo_vendas(self):
        arquivo = 'tbvendas.csv'
        Arquivo.criar_arquivo(self, arquivo)

        arquivo = open(arquivo, 'a')
        escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')

        numero = 'NUMERO'

        cod_cliente = 'CODCLI'
        cliente = 'CLIENTE'
        cidade = 'CIDADE'
        estado = 'UF'
        canalvenda = 'CANAL VENDA'

        cod_produto = 'CODPRO'
        produto = 'PRODUTO'
        categoria = 'CATEGORIA'
        qtde = 'QTDE'
        preco = 'PREÇO'

        tabela = [  numero, cod_cliente, cliente, cidade, estado, canalvenda, 
                    cod_produto, produto, categoria, qtde, preco]
        escritor.writerow(tabela)
        

    def criar_arquivo_compras(self):
        arquivo = 'tbcompras.csv'
        Arquivo.criar_arquivo(self, arquivo)

        arquivo = open(arquivo, 'a')
        escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')

        numero = 'NUMERO'

        cod_forn = 'CODFOR'
        fornecedor = 'FORNECEDOR'
        cidade = 'CIDADE'
        estado = 'UF'
        tipoforn = 'TIPO FORN'
        
        cod_produto = 'CODPRO'
        produto = 'PRODUTO'
        categoria = 'CATEGORIA'
        qtde = 'QTDE'
        preco = 'PREÇO'

        tabela = [  numero, cod_forn, fornecedor, cidade, estado, tipoforn, 
                    cod_produto, produto, categoria, qtde, preco]
        escritor.writerow(tabela)


    def criar_arquivo_contas_receber(self):
        arquivo = 'tbreceber.csv'
        Arquivo.criar_arquivo(self, arquivo)

        arquivo = open(arquivo, 'a')
        escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')

        numero = 'NUMERO'

        cod_cliente = 'CODCLI'
        cliente = 'CLIENTE'
        cidade = 'CIDADE'
        estado = 'UF'
        canalvenda = 'CANAL VENDA'

        parcela = 'PARCELA'
        valor = 'VALOR'
        vencimento = 'VENCIMENTO'
        numparc = 'NUMPARC'
        status = 'STATUS'

        tabela = [  numero, cod_cliente, cliente, cidade, estado, canalvenda, 
                    parcela, valor, vencimento, numparc, status]
        escritor.writerow(tabela)


    def criar_arquivo_contas_pagar(self):
        arquivo = 'tbpagar.csv'
        Arquivo.criar_arquivo(self, arquivo)

        arquivo = open(arquivo, 'a')
        escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')

        numero = 'NUMERO'

        cod_forn = 'CODFOR'
        fornecedor = 'FORNECEDOR'
        cidade = 'CIDADE'
        estado = 'UF'
        tipoforn = 'TIPO FORN'

        parcela = 'PARCELA'
        valor = 'VALOR'
        vencimento = 'VENCIMENTO'
        numparc = 'NUMPARC'
        status = 'STATUS'

        tabela = [  numero, cod_forn, fornecedor, cidade, estado, tipoforn, 
                    parcela, valor, vencimento, numparc, status]
        escritor.writerow(tabela)
