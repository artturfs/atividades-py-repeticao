n = int(input("Quantos números da sequência de Fibonacci você deseja: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()