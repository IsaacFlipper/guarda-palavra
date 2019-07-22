def escrever(palavra): # função de escrever no arquivo de texto

	escrever = open('palavra.txt', 'a') # monta o caminho do arquivo

	escrever.write(palavra+'\n') # escreve no arquivo o que tem na variavel palavra

	escrever.close() # fechara o arquivo para não dar conflito ou da erro

def ler(palavra): # função de ler o arquivo de texto
	ler = open('palavra.txt', 'r') # monta o caminho do arquivo

	ler = ler.readlines() # monta o arquivo para ser lido linha por linha

	igual = 0 # contador de controle

	for i in range(len(ler)): # for que vai ver se a palavra nova é repetida ou não 

		if ler[i] == palavra+'\n': # se for repetida ela vai adicionar um 1 a mais na variavel "igual" e vai dar um break que vai para o for

			igual += 1

			break

		else: # se não ele so vai dar um pass

			pass

	if igual == 0: # se a variavel de controle for igual a 0 ele escrever uma nova palavra

		escrever(palavra)

		print('pronto!')

	else: # se não ele não adiciona ao txt
	
		print('já existe!')

