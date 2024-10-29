palavra = input("Digite uma palavra: ")
palavra_invertida = ''.join(reversed(palavra))  # reversed() para inverter a palavra

if palavra == palavra_invertida:
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")