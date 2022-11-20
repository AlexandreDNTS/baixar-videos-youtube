import PySimpleGUI as sg
from importlib.resources import path
from pytube import YouTube


def tela_inicial():
    layout = [
        [sg.Text('BAIXAR VÍDEOS DO YOUTUBE')],
        [sg.Text('\n\n')],
        [sg.Button('baixar mp3')]
    ]
    return sg.Window('Baixar Vídeos do youtube', layout=layout, finalize=True)


def baixar_video():
    layout = [
        [sg.Text('BAIXAR VÍDEOS DO YOUTUBE')],
        [sg.Text('\n\n')],
        [sg.Text('url '), sg.Input(key='url'), sg.Text(
            'caminho'), sg.Input(key='caminho')],
        [sg.Button('BAIXAR'), sg.Button('cancelar')]
    ]
    return sg.Window('baixar videos', layout=layout, finalize=True)


telainicial, baixarvideo = tela_inicial(), None

while True:
    window, eventos, valores = sg.read_all_windows()
    if window == telainicial and eventos == sg.WIN_CLOSED or window == baixarvideo and eventos == sg.WIN_CLOSED:
        break
    if window == telainicial and eventos == 'baixar mp3':
        baixarvideo = baixar_video()
        telainicial.hide()
    if window == baixarvideo and eventos == 'cancelar':
        baixarvideo.hide()
        telainicial.un_hide()
    if window == baixarvideo and eventos == 'BAIXAR':
        yt = YouTube(valores['url'])
        ys = yt.streams.get_highest_resolution()
        ys.download(valores['caminho'])
