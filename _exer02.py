#calcular indice de massa corporal IMC
# IMC = peso / (altura*altura)

nome = (input ("Digite seu nome: "))
altura = float (input ("Digite sua altura: "))
peso = float (input ("Digite seu peso: "))
imc = peso / (1.83*1.83)



print(nome, "tem", altura, "de altura", "pesa", peso, "quilos, e seu IMC é:", round(imc, 2))

if imc <= 16:
    classificacao = "Magreza grau 1"
elif imc <= 25:
    classificacao = "Pré-obesidade"
elif imc <= 35:
    classificacao = "Obesidade moderada"
elif imc <= 40:
    classificacao = "Obesidade severa"
else:
    classificacao = "Obesidade muito severa"
print("Classificação:", classificacao)
