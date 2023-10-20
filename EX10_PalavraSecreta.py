import os

palavra_secreta = 'perfume' #Variável fica onde armazenada a palavra secreta.
letras_acertadas = '' #Armazena as letras corretas, digitadas pelo usuário.
tentativas = 0 #Contabiliza o número de tentativas.

while True:  #Início do laço de repetição do jogo.
    
    letra_digitada = input('Digite uma letra: ') #Pede para que o usuário digite apenas UMA letra.
    tentativas += 1
    
    if len(letra_digitada) > 1: #Caso o usuário digite mais que um caractere, ele pede para digitar apenas UM, e volta para o começo.
        print('Digite apenas UMA letra.')
        continue

    if letra_digitada in palavra_secreta: #Verifica se a letra que foi digitada, faz parte da palavra secreta.
        letras_acertadas += letra_digitada #Caso faça, a letra é armazenada.

    palavra_formada = '' #Variável para formar a palavra atráves das letras digitadas.
    for letra_secreta in palavra_secreta: #Para cada letra que for inserida,
        if letra_secreta in letras_acertadas: #Se a letra estiver entre as letras corretas,
            palavra_formada += letra_secreta # A letra é adicionada na variável Palavra_formada,
        else: # Caso não seja correta, será adicionado * na Palavra_formada.
            palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}') # Da para o usuário, um feedback de como está o progresso dele no jogo.
    
    if palavra_formada == palavra_secreta: # Caso o usuário acerte todas as letras, ele é parabenizado.
        os.system('cls')
        print(f'Parabéns você acertou, a palavra era: {palavra_secreta}\n' f'O número de tentativas foram: {tentativas}')
        letras_acertadas = '' #Zera as letras corretas
        tentativas = 0 #Zera o número de tentativas.