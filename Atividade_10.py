#Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo” caso contrário
numero = int(input("Digite o valor: "))
if numero >= 0 and numero <= 10:
    print("Dentro do Intervalo!!!")
else:
    print("Fora do intervalo...")