LENDO UM BOTÃO

COMENTÁRIOS:

1. Funções utilizadas
GPIO.setmode(<opção>) - Realiza as configurações iniciais do GPIO
	Opções:
	GPIO.BOARD - Utiliza a numeração dos pinos da placa PCB, no caso do Raspberry
		Pi3 possui um GPIO de 40 pinos. 
	GPIO.BCM - Utiliza a numeração BCM, para saber digite o comando $gpio readall
		e veja o nome do GPIO correspondente no campo 'name'.
		O pino de saída para uma mesma porta pode variar com o modelo do Raspberry.

GPIO.setup(<chanel>, <opção 1>, <opção 2>) - Configuração do pino
	Opções:
	<chanel> - Recebe um número inteiro relativo a porta, podendo ser utilizada a
		numeração BCM ou Board como configurado em setmode()
	<opção 1>
		GPIO.IN - Configura o pino como entrada
	<opção 2>
		pull_up_down=GPIO.PUD_UP - Habilita o resistor de Pull-up
		pull_up_down=GPIO.PUD_DOWN - Habilita o resistor de Pull-down
		Os resistores de Pull-up e down só podem ser urilizados quando o pino está
		configurado como entrada. Possuem o valor de 10Kohm.

GPIO.add_event_detect(<chanel>, <detecção>, <desvio>) - Adiciona um novo evento
a porta indicada.
	<chanel> - Recebe um número inteiro relativo a porta  
	<detecção>
		GPIO.FALLING - Dispara o evento pela detecção da borda de descida
		GPIO.RISING - Dispara o evento pela detecção da borda de subida
		GPIO.BOTH - Dispara o evendo pela detecção da borda de subida ou descida
	<desvio>
	callback=my_callback - Realiza a chamada da função callback

2. Tratamento de Debouce
	O ruído provocado pelo aperto da tecla faz que o evento dispare mais de uma vez,
já que a velocidade do processador é mais rápida que o tempo de duração do ruído.
Podemos realizar o tratamento do debouce por hardware ou software. Por software é 
feita duas leituras do pino espaçadas normalmente por um tempo de 20ms para chegar
se o pino possui o mesmo estado. Por hardware é inserido um capacitor em série ao
resistor de pull-up, normalmente a constante RC é dada por um valor de 10ms. Assim,
utilizando o resistor interno de pull-up pode ser utilizado um capacitor de 1uF
em paralelo com o botão.  


