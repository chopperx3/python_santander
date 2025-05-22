print("EJERCICIO 1 FOR\nFrutas:\n")
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(f"- {fruta}")

print("\n------------------------")

print("EJERCICIO 2 FOR\nNúmeros multiplicados por 2:\n")
for numero in range(5):
    print(f"Valor: {numero * 2}")

print("\n------------------------")

print("EJERCICIO 3 FOR\nNumeros impares:\n")

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)    

print("\n------------------------")

print("EJERCICIO 1 WHILE\nContador multiplicado por 2:\n")
contador = 1
while contador <= 5:
    print(f"Contador: {contador * 2}")
    contador += 1

contador = 0

print("\n------------------------")

print("EJERCICIO 2 WHILE\nContador multiplicado por 2:\n")

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break