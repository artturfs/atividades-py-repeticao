n = int(input("Quantos termos deseja gerar? "))
a1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

for i in range(n):
    termo = a1 + i * razao
    print(termo, end=' ')
print()
