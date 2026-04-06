#Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe “Número inválido"
valor = int(input("Digite o valor: "))
if valor >= 0:
    mult = valor ** 0.5
    print("A raiz aproximada é: ",mult)
else:
    print("Número inválido.")