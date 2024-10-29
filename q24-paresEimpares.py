pares = 0
impares = 0

for _ in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números pares:", pares)
print("Números ímpares:", impares)
