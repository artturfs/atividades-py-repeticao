n = int(input("Quantos números você irá digitar? "))
maior = float('-inf')
menor = float('inf')

for _ in range(n):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Maior número:", maior)
print("Menor número:", menor)
