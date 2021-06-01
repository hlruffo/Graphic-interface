import requests
import json
from PySimpleGUI import PySimpleGUI as sg
import time


#extrair para cota dolar 
# lógica que quero implementar no output-> se marcado no checkbox = TRUE chamar função 

def dolar():
    cotas = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotas = cotas.json()
    cota_dolar = cotas['USDBRL']['bid']
    print(f'A cotação do Dólar é {cota_dolar} Reais.\n')
    

#extrair para cota euro
def euro():
    cotas = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotas = cotas.json()
    cota_euro = cotas['EURBRL']['bid']
    print(f'A cotação do Euro é {cota_euro} Reais.\n')

#extrair para cota bitcoin
def bitcoin():
    cotas = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotas = cotas.json()
    cota_bitcoin = cotas['BTCBRL']['bid']
    print(f'A cotação do Bitcoin é :{cota_bitcoin} Reais.\n')



class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(25,0),key='nome')],
            [sg.Text('Selecione a cotação desejada:')],
            [sg.Checkbox('Dólar', key='dolar'),sg.Checkbox('Euro', key='euro'),sg.Checkbox('Bitcoin', key='bitcoin')],
            [sg.Button('Receber informação')],
            [sg.Output(size=(40,20))]
        ]

        #janela
        self.janela = sg.Window("Cotações",).layout(layout)

        

    def Iniciar(self):
        while True:
            #extrair dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            informar_dolar = self.values['dolar']
            informar_euro = self.values['euro']
            informar_bitcoin = self.values['bitcoin']
            A = time.strftime('%H:%M:%S', time.localtime())
            B = time.strftime('%d-%m-%y', time.localtime())


            print(f'Olá {nome},\n às {A} de {B} ')
            
            if informar_dolar == True:
                dolar()
            if informar_euro == True:
                euro()
            if informar_bitcoin == True:
                bitcoin()


tela = TelaPython()
tela.Iniciar()

"""


"""