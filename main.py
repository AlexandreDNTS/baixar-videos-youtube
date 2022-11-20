import PySimpleGUI as sg
from pytube import YouTube


def tela_inicial():
    layout = [
        [sg.Text('BAIXAR VÍDEOS DO YOUTUBE')],
        [sg.Text('\n\n')],
        [sg.Button('baixar mp3')]
    ]
    return sg.Window('Baixar Vídeos do youtube', layout=layout, finalize=True)


telainicial = tela_inicial()

while True:
    window, eventos, valores = sg.read_all_windows()
    if window == telainicial and eventos == sg.WIN_CLOSED:
        break
