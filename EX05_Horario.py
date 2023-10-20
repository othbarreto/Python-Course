"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input("Digite a hora atual em numero inteiro: ")


try:
    horario_int = int(entrada)

    manha = horario_int >= 0 and horario_int <= 11
    tarde = horario_int >= 12 and horario_int <= 17
    noite = horario_int >= 18 and horario_int <= 23

    if manha:
        print("Bom dia")
    elif tarde:
        print("Boa tarde")
    elif noite:
        print("Boa noite")
    else:
        print("Não connheço essa hora")

except:
    print("Você não digitou um horario")

