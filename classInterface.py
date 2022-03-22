from classValidacoes import *
import datetime
data_hora_atuais = datetime.datetime.now()
data_hora_pt_BR = data_hora_atuais.strftime(' %d/%m/%Y %H:%M:%S')


tamanho = 100


class Interface:

    def __init__(self, cores):
        self.cores = cores


    def incrementar_linha(self, tamanho=42, caracter='-'):
        return caracter * tamanho


    def apresentar_cabecalho_sistema(self, texto='', versao='v1.0 '):
        tam = int(tamanho / 2)
        caracter = '='
        print(f'{bgCor[2]}{Interface.incrementar_linha(self, tamanho, caracter)}{bgCor[0]}')
        texto = texto.center(tamanho)
        print(f'{bgCor[2]}{texto}{bgCor[0]}')
        print(f'{bgCor[2]}{data_hora_pt_BR.ljust(tam)}{versao.rjust(tam)}{bgCor[0]}')
        print(f'{bgCor[2]}{Interface.incrementar_linha(self, tamanho, caracter)}{bgCor[0]}')


    def apresentar_cabecalho_interno(self, texto='', cor=(bgCor[0])):
        print(Interface.incrementar_linha(self, tamanho))
        print(texto.center(tamanho), cor)
        print(Interface.incrementar_linha(self, tamanho))


    def apresentar_menu_principal(self, lista, menu):
        Interface.apresentar_cabecalho_interno(self, menu)
        contador = 1
        for item in lista:
            print(f'{fontCor[3]}{contador:>10}{bgCor[0]} - {fontCor[4]}{item}{bgCor[0]}')
            contador += 1
        print(Interface.incrementar_linha(self, tamanho, '~'))
        opcao = Validacoes.validar_numero_inteiro(self, f'{fontCor[3]}Digite a opção desejada: {bgCor[0]}')
        return opcao
