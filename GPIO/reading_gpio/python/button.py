#****************************************************************
#                       LENDO UM BOTÃO
#****************************************************************
#!/usr/bin/python3 
 
#************************* MÓDULOS ******************************
import RPi.GPIO as GPIO        #Módulo da porta GPIO
import time                    #Biblioteca de tratamento de tempo
#****************************************************************

#****************** CONSTANTES E VARIÁVEIS **********************
CHAVE = 32          #Pino onde será inserido o botão
#****************************************************************

#******************** ENTRADAS E SAÍDAS *************************
GPIO.setmode(GPIO.BOARD)	#BOARD faz referência ao número do pino na PCB
GPIO.setup(CHAVE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#Configura como entrada e habilita o pull-up

#****************************************************************

#************************** FUNÇÕES *****************************
def my_callback(channel):			#Função de tratamento da tecla
    print('You pressed the button')
#****************************************************************

#************************** EVENTOS *****************************
GPIO.add_event_detect(CHAVE, GPIO.FALLING, callback=my_callback) 
	#Evento da tecla, borda de descida
#****************************************************************

#************************ MAIN CODE *****************************
print ("Aguardando precionar o botão.")
print ("Precione CRT+C para sair.")

i = 0
while True:
	i = i + 1
	print(i)
	time.sleep(1)


