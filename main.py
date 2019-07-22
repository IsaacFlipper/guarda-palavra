from funcao import *
'''
\------------------------------------------------------------------------------------------------------------------------------------/
Este programa foi criado para me ajudar com as palavras do ingles palavras novas para mim apreder o significado mais boa parte das vez
eu acabava esquecendo de pesquisar o significado então pensei e se eu criar um programa que liste palavras novas e que não se repita 
então resolvi fazer sei que não é muita coisa mais para quem começou a pouco tempo já é um grande avanço eu estou bem orgulhoso de mim 
mesmo tomara que alguem ache legal esta função bem basica e simples
/------------------------------------------------------------------------------------------------------------------------------------\
'''
print('//'*40)
print('se quiser sair digite sair:')
print('//'*40)

nome = str(input('digite algo:\n>>>'))

while nome not in 'sair':
    ler(nome)
    nome = str(input('digite algo:\n>>>'))

print('programa encerrado! ')

