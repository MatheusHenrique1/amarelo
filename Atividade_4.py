#Leia um número e informe se ele é par ou ímpar.
numero = int(input("Informe o número: "))
if numero % 2 == 0:
    print("O número é par!")
elif numero % 2 != 0:
    print("O número é impar!")
else:
    print("Resultado errado.")