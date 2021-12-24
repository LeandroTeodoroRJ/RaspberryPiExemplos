#**********************************************************
#    EXEMPLO DE INTERRUPÇÕES UTILIZANDO TIMERS
#**********************************************************
'''
Placa: Raspberry Pi3 model B+ 
OS: Raspbian versão 10
Python versão 3.7.3
'''

from threading import Timer
import time

flag_interrupcao = True

def evento_timer1():
    print ("Interrupção Timer 1")
    timer1 = Timer(2.0, evento_timer1)
    if (flag_interrupcao == True):
        timer1.start()
    else:
        timer1.cancel()

def evento_timer2():
    print ("Interrupção Timer 2")
    timer2 = Timer(10.0, evento_timer2)
    if (flag_interrupcao == True):
        timer2.start()
    else:
        timer2.cancel()
 

evento_timer1()
evento_timer2()

cont = 0
while (cont<25):
    time.sleep(1)
    print("Loop principal")
    cont = cont+1
flag_interrupcao = False

