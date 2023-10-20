nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f'Seu nome é: {nome}') #Exibe o nome do usuário.
    print(f'Seu noome invertido é: {nome[::-1]}') # Com o passe em -1 ele começa a exibir o conteúdo da variável de trás para frente.

    if " " in nome: # Esse bloco de IF está verificando se no NOME contém ou não espaços.
        print('Seu nome contém espaços.')
    else:
        print('Seu nome NÃO contém espaços.')   

    print(f'Seu nome tem {(len(nome))} letras.') # A função LEN está sendo utilizada para contar as letras da variável.
    print(f'A primeira letra do seu nome é: {nome[0]}') # O índice 0 retorna a primeira letra da variável.
    print(f'A última letra do seu nome é: {nome[-1]}') # O índice -1 retorna a última letra da variável.
    
else:
    print("Você deixou campos em branco.")