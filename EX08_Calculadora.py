while True: #Inicio do laço de Repetição.

    num1 = input("Digite um número: ")
    num2 = input("Digite um número: ")
    operador = input("Selecione um operação + - / * :")

    numeros_validos = None # Flag para identificação se os números são válidos ou não.
    float_num1 = 0 
    float_num2 = 0

    try: 
        float_num1 = float(num1) #Convertendo número string para float.
        float_num2 = float(num2) #Convertendo número string para float.
        numeros_validos = True # Validando os números.

    except:
        
        numeros_validos = None # Identificação de números inválidos.

    if numeros_validos is None: # Após a identificação dos números inválidos, esse bloco informa que tem algo errado.

        print('Um ou ambos os números digitados são inválidos!')
        continue

    operadores_validos = '+ - / *' # Validando os operadores aceitos no programa.

    if operador not in operadores_validos: # Caso haja o usuário digite um operador inválido, ele caíra nesse bloco, que informa o erro.
        print('Operador inválido!')
        continue

    if len(operador) > 1: # Se o usuário digitar mais que um operador, o programa não aceita e informa o erro.
        print('Digite apenas uma operador!')
        continue

    if operador == "+":
        soma = float_num1 + float_num2
        print(f' O resultado de {num1} {operador} {num2} é: {soma}')
    elif operador == "-":
        sub = float_num1 - float_num2
        print(f' O resultado de {num1} {operador} {num2} é: {sub}')
    elif operador == "/":
        divisao = float_num1 / float_num2
        print(f' O resultado de {num1} {operador} {num2} é: {divisao}')
    elif operador == "*":
        multi = float_num1 * float_num2
        print(f' O resultado de {num1} {operador} {num2} é: {multi}')  


    sair = input('Quer sair? [s]im: ').lower().startswith('s') # Verifica se o usuário deseja permanecer no programa. .lower transforma o que foi digitado em minúsculo, .startwith verifica se o que foi digitado começa com "s".

    if sair is True: # Caso o que foi digitado for 'Sair' ou começar com 'S' o programa se encerra.
        print('Encerrando...')
        break  

