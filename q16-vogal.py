vogais = "aeiou"
texto = input("Digite uma frase: ").lower()
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print(f"Número de vogais: {contador}")