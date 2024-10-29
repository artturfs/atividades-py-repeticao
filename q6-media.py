ac = 0

for i in range(1, 6):
    x = int(input(f"Digite a {i} nota: "))
    ac += x
print("Sua média foi :", ac / i)