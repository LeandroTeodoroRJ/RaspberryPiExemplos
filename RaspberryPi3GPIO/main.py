#*******************************************************************
#                  RASPBBERRRY PI 3 - GPIO
#*******************************************************************
# -*- coding: utf-8 -*-
'''
Exemplo para manipulação das portas GPIO do Raspberry Pi3.
OBS:
1) As portas possuem tensão  de saída de 3,3V@50mA.
2) Pinagem dos pinos do GPIO no arquivo GPIO_Pinout.png
3) Utilizazar GPIO.setmode(GPIO.BCM)ou GPIO.setmode(GPIO.BOARD).
Existem dois modos de numeração para BOARD e BCM.
4) Habilite as portas GPIO em Preferences -> Rasp pi Config ->
Interfaces -> Remote GPIO
5) Utiliza o comando gpio readall no shell console do raspian
para verificar as mudanças das portas.
6) A numeração em BCM é mostrada com o comando gpio readall.
'''
#************************* MÓDULOS ********************************
import RPi.GPIO as GPIO   #Módulo de controle das portas GPIO
import time               #Para uso de delay
#******************************************************************

#****************** CONSTANTES E VARIÁVEIS ************************
LED = 16	#Saída para o led, pino 36 
CHAVE = 12
DELAY_TIME = 3
#******************************************************************

#******************** ENTRADAS E SAÍDAS ***************************
GPIO.setmode(GPIO.BCM)    #Configura o GPIO para ser usado como portas paralelas
GPIO.setup(LED, GPIO.OUT)  #Configura a porta GPIO 16(pino 36) como saída
GPIO.setup(CHAVE, GPIO.IN)   #Configura a porta GPIO 12 como entrada
#******************************************************************

#************************ MAIN CODE *******************************
for porta in range(0,3):  #loop por 3 vezes
    print('Porta em nível alto')
    GPIO.output(LED, GPIO.HIGH)			#Coloca o pino em nível alto   
    time.sleep(DELAY_TIME)         	#Delay 3 segundos
    print('Porta em nível baixo')
    GPIO.output(LED, GPIO.LOW)			#Coloca o pino em nível baixo
    time.sleep(DELAY_TIME)
    
if (GPIO.input(CHAVE) == True):			#Testa a chave de entrada
    print('A porta de entrada esta em nível alto')
else:
    print('A porta de entrada esta em nível baixo')

GPIO.cleanup()  #Fecha a porta encerrando o processo.

#******************************************************************
