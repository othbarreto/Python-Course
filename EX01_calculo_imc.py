print("Vamos calcular o seu IMC\n")

nome = str(input("Qual o seu nome? "))
altura = float(input("Qual sua altura em metros ? "))
peso = float(input("Qual seu peso em kilos ?"))
linha = ""

calculo_imc = peso / (altura * altura)
imc = float(f"{calculo_imc:.2f}")


print(
       f"{linha:=^40}.\n"
       f"{nome} tem {altura}m de altura \n"
       f"Pesa {peso}kg e seu IMC é de {imc} \n"
       f"{linha:=^40}.\n"
       )

if imc < 18.5:
       print("ABAIXO DO NORMAL")
elif 18.5 <= imc < 24.9:
       print("NORMAL")
elif 25 <= imc < 29.9:
       print("SOBREPESO")
elif 30 <= imc < 34.9:
       print("OBESIDADE GRAU 1")
elif 35 <= imc < 39.9:
       print("OBESIDADE GRAU 2")
elif imc > 40:
       print(" OBESIDADE GRAU 3")
