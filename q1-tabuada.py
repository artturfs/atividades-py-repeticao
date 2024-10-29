print("Escolha uma alternativa para a tabuada:")
print("\na) Soma")
print("b) Subtração")
print("c) Multiplicação")
print("d) Divisão")

alternativa = str(input("Digite a alternativa: "))
numero = int(input("Agora, digite o número para a tabuada: "))

if alternativa == "a":
    print(f"A tabuada de {numero} é: ")
    for i in range(1, 11):
        print(f"{numero} + {i} = {numero + i}")

if alternativa == "b":
    print(f"A tabuada de {numero} é: ")
    for i in range(1, 11):
        print(f"{numero} - {i} = {numero - i}")

if alternativa == "c":
    print(f"A tabuada de {numero} é: ")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if alternativa == "d":
    print(f"A tabuada de {numero} é: ")
    for i in range(1, 11):
        print(f"{numero} / {i} = {numero / i}")
