from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme("Reddit")
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(30,1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*',size=(30,1))],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')],
]
#janela
janela = sg.Window('Tela de Login', layout)

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Hugo' and valores['senha'] == '0913':
            print('Bem vindo Hugo')