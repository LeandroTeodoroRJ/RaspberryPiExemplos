#**************************************************************************
#                    RASPBERRY PI 3 - PORTA PWM
#**************************************************************************
#OBS:
#Python versão: 3.7.3
#Raspberry versão: Pi3 Model b
#Saída no PWM no pino 32
#**************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*

import RPi.GPIO as gpio    #Modulo das portas de uso geral

#**************************************************************************
#CONSTANTES E DEFINIÇÕES
resolucao = '190x140+20+20'
canal_pwm = 12

#**************************************************************************
# Variáveis Globais
duty_cicle = 50.0

#***************************************************************************
#CONFIGURAÇÃO DO PWM
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)     #Desabilita os alertas de porta em uso
gpio.setup(12,gpio.OUT)		#Configura o pino como saída
freq = float(input("Insira a frequência do PWM[Hz]: "))
pwmRed = gpio.PWM(canal_pwm, freq) #Instancia o objeto, parâmetros (canal, frequencia)
pwmRed.start(duty_cicle)


#EVENTOS
def clica_bt2(event):
    global duty_cicle
    duty_cicle = duty_cicle*1.1
    if (duty_cicle > 100.0):
        duty_cicle = 99
    pwmRed.ChangeDutyCycle(duty_cicle)
    print("Duty Cicle atual: ", duty_cicle)

def clica_bt3(event):
    global duty_cicle
    duty_cicle = duty_cicle*0.9
    pwmRed.ChangeDutyCycle(duty_cicle)
    print("Duty Cicle atual: ", duty_cicle)

def clica_bt4(event):
    global duty_cicle
    duty_cicle = duty_cicle*1.01
    if (duty_cicle > 100.0):
        duty_cicle = 99
    pwmRed.ChangeDutyCycle(duty_cicle)
    print("Duty Cicle atual: ", duty_cicle)

def clica_bt5(event):
    print('Clicou no Botão Desce 1%.')
    global duty_cicle
    duty_cicle = duty_cicle*0.99
    pwmRed.ChangeDutyCycle(duty_cicle)
    print("Duty Cicle atual: ", duty_cicle)

#****************************************************************************
#GUI
janela = Tk()
janela.geometry(resolucao)


lb1 = Label(janela, text='Raspberry Pi3 - Porta PWM')
lb2 = Label(janela, text=' ')
lb5 = Label(janela, text=' ')


bt2 = Button(janela, text='Sobe 10%', width=10)
bt3 = Button(janela, text='Desce 10%', width=10)
bt4 = Button(janela, text='Sobe 1%', width=10)
bt5 = Button(janela, text='Desce 1%', width=10)


bt2.bind('<Button-1>', clica_bt2)
bt3.bind('<Button-1>', clica_bt3)
bt4.bind('<Button-1>', clica_bt4)
bt5.bind('<Button-1>', clica_bt5)


#****************************************************************************
#Layout
lb1.grid(row=0, column=0, sticky=W, columnspan=2)
lb2.grid(row=1, column=0, sticky=W)
bt2.grid(row=2, column=0, sticky=W)
bt3.grid(row=2, column=1, sticky=W)
lb5.grid(row=3, column=0, sticky=W)
bt4.grid(row=4, column=0, sticky=W)
bt5.grid(row=4, column=1, sticky=W)

#******************************************************************************
#Run
janela.mainloop()
