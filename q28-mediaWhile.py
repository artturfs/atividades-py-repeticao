soma = 0
contador = 0

while True:
    numero = input("Digite um número (ou 'fim' para encerrar): ")
    if numero == 'fim':
        break
    soma += int(numero)
    contador += 1

media = soma / contador if contador > 0 else 0
print("A média é:", media)  