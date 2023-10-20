# PROGRAMA PARA ANALISAR REPETIÇÃO DE LETRAS.

frase = 'Thiago Barreto dos Santos'

i = 0 # Iniciando o Indice com 0
qtd_que_apareceu = 0 # Essa variavel armazenará, a quantidade de vezes que a letra apareceu.
letra_apareceu_mais_vezes = '' # Essa variavel armazenará, a que mais letra apareceu.

while i < len(frase): # Enquanto i for menor que a quantidade de caracteres da frase, o laço continua rodando.

    letra_atual = frase[i] #Verifica a letra atual com base no Indice.

    if letra_atual == ' ': #Esse bloco If, pulará todos os caracteres em branco.
        i += 1 
        continue

    qtd_atual = frase.count(letra_atual) # Armazena a quantidade de vezes que a letra atual apareceu.

    if qtd_que_apareceu < qtd_atual:
        qtd_que_apareceu = qtd_atual 
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_que_apareceu}x'
)