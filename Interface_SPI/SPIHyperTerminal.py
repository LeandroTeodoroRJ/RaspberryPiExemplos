#*************************************************************************************************
#                        HYPER TERMINAL SPI PARA RASPBERRY PI3 MODEL B+
#*************************************************************************************************
# Status: Em desenvolvimento

#import tkinter as tk    #Importa a biblioteca tkinter e nomeia como tk
#from tkinter import*
#from tkinter.ttk import*

from tkinter import*
from tkinter.ttk import*
import time
#import spidev

#Funções
#def action_open_window(event):
    #ed_freq_clock.insert(1, '5000')
#    pass

def bt_brir_porta_click():
#    spi = spidev.SpiDev()
    speed_clock = int(ed_freq_clock.get())       #Converte o valor digitado no edit para inteiro
#   spi.max_speed_hz = speed_clock
    device = int(slave_dev.get())
    if (porta.get() == 'SPI0'):
        bus = 0
    elif (porta.get() == 'SPI1'):
        bus = 1
    else:
        bus = 2
#   spi.open(bus, device)
    if ( idle.get() == 'Baixo' and aquisicao.get() == 'Idle para Ativo'):
#       spi.mode = 0b00
        print(00)
    elif (idle.get() == 'Baixo' and aquisicao.get() == 'Ativo para Idle'):
#       spi.mode = 0b01
        print(1)
    elif ( idle.get() == 'Alto' and aquisicao.get() == 'Idle para Ativo'):
#       spi.mode = 0b10
        print(10)
    else:   #( idle.get() == 'Alto' and aquisicao.get() == 'Ativo para Idle')
#       spi.mode = 0b11
        print(11)

def bt_fechar_porta_click():
#   spi.close()
    pass

def bt_enviar_click():
    delay = int(ed_delay.get())
    bytes_rx = int(ed_num_bytes_rx.get())
    send_string = tbox_enviado.get(1.0, END)
    to_send = list(map(int,send_string.split()))
    print(to_send)
#    spi.xfer(to_send)
    time.sleep(delay/1000)      #Delay milisegundos
#   lista_rx = spi.readbytes(bytes_rx)
#   print(lista_rx)

#GUI
janela = Tk()        #Instancia a variável janela como uma classe Tk
janela.title('Hyper Terminal SPI')    #Título superior da janela

#Configurações da janela
janela.geometry('450x350+0+0')  # 'LARGURAxALTURA+DISTÂNCIA_ESQUERDA+DISTÂNCIA_DO_TOPO'
                                    #passado em formato string. Medidas em pixels.
janela.resizable(height = False, width = False)  #Desabilita o remimensionamento da janela

#Widgets
lb_porta = Label(janela, text='Escolha a porta SPI que será utilizada: ')
lb_slave = Label(janela, text='Dispositivo slave para comunicação: ')
lb_max_speed = Label(janela, text='Velocidade de clock[Hz]: ')
lb_clock_idle = Label(janela, text='Nível do clock em idle: ')
lb_aquisicao = Label(janela, text='Borda de aquisição de dados: ')
lb_delay = Label(janela, text='Delay para recemimento de dados[ms]: ')
lb_num_bytes_rx = Label(janela, text='Número de bytes que serão recebibos: ')
lb_bytes_enviados = Label(janela, text='Bytes enviados: [Enviar em decimal separado por espaço]')
lb_bytes_recebidos = Label(janela, text='Bytes recebibos: ')
bt_abrir_porta = Button(janela, text='Abrir Porta SPI', width=35, command=bt_brir_porta_click)
bt_fechar_porta = Button(janela, text='Fechar Porta SPI', width=35, command=bt_fechar_porta_click)
bt_enviar = Button(janela, text='Enviar', width=15, command=bt_enviar_click)
ed_freq_clock = Entry(janela, width=32)
ed_freq_clock.insert(0, '5000')
ed_delay = Entry(janela, width=32)
ed_delay.insert(0, '0')
ed_num_bytes_rx = Entry(janela, width=32)
ed_num_bytes_rx.insert(0, '0')

porta = StringVar()
op_cb_porta = ['SPI0','SPI1','SPI2']
cb_porta = Combobox(janela, values=op_cb_porta, textvariable=porta,  state='readonly', width=32)
cb_porta.current(0)        #Define a primeira opção como default

idle = StringVar()
op_clock_idle = ['Baixo','Alto']
cb_clock_idle = Combobox(janela, values=op_clock_idle, textvariable=idle, state='readonly', width=32)
cb_clock_idle.current(0)        #Define a primeira opção como default

aquisicao = StringVar()
op_aquisicao = ['Idle para Ativo','Ativo para Idle']
cb_aquisicao = Combobox(janela, values=op_aquisicao, textvariable=aquisicao, state='readonly', width=32)
cb_aquisicao.current(0)        #Define a primeira opção como default


slave_dev = StringVar()
op_cb_slave = ['0','1','2']
cb_slave = Combobox(janela, values=op_cb_slave, textvariable=slave_dev,  state='readonly', width=32)
cb_slave.current(0)        #Define a primeira opção como default



rolbar1 = Scrollbar(janela, orient=VERTICAL)   #Define a orientação vertical para a barra de rolagem
rolbar2 = Scrollbar(janela, orient=VERTICAL)   #Define a orientação vertical para a barra de rolagem
tbox_enviado = Text(janela, wrap=WORD, width=55, height=3, yscrollcommand=rolbar1.set)
rolbar1.config(command=tbox_enviado.yview)   #Define que a barra de rolagem será anexada
                                                    #ao objeto Caixa_de_texto (text).
tbox_recebido = Text(janela, wrap=WORD, width=55, height=3, yscrollcommand=rolbar2.set)
rolbar2.config(command=tbox_recebido.yview)

#Layout
lb_porta.grid(row=0, column=0, sticky=W)
cb_porta.grid(row=0, column=1, sticky=W)
lb_slave.grid(row=1, column=0, sticky=W)
cb_slave.grid(row=1, column=1, sticky=W)
lb_max_speed.grid(row=2, column=0, sticky=W)
ed_freq_clock.grid(row=2, column=1, sticky=W)
lb_clock_idle.grid(row=3, column=0, sticky=W)
cb_clock_idle.grid(row=3, column=1, sticky=W)
lb_aquisicao.grid(row=4, column=0, sticky=W)
cb_aquisicao.grid(row=4, column=1, sticky=W)
lb_delay.grid(row=5, column=0, sticky=W)
ed_delay.grid(row=5, column=1, sticky=W)
lb_num_bytes_rx.grid(row=6, column=0, sticky=W)
ed_num_bytes_rx.grid(row=6, column=1, sticky=W)
bt_abrir_porta.grid(row=7, column=0, sticky=W)
bt_fechar_porta.grid(row=7, column=1, sticky=W)
lb_bytes_enviados.grid(row=8, column=0, sticky=W, columnspan=2)
tbox_enviado.grid(row=9, column=0, sticky=W, columnspan=2)
bt_enviar.grid(row=10, column=0, sticky=W)
lb_bytes_recebidos.grid(row=11, column=0, sticky=W)
tbox_recebido.grid(row=12, column=0, sticky=W, columnspan=2)

#Eventos
#janela.bind("<Visibility>", action_open_window)             #Evento de fechar a aberta



janela.mainloop()      #Abre a janela e interrompe o script enquanto a janela estiver sendo exibida
