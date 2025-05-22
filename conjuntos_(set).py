#Un conjunto es una estructura de datos mutable y no ordenada que permite almacenar una colección de elementos únicos. 
#Los conjuntos se encierran entre llaves {} o se crean utilizando la función set().

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}x

#add(elemento): agrega un elemento al conjunto.
#remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
#discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
#clear(): elimina todos los elementos del conjunto.

frutas = {"manzana", "banana", "naranja"}

frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()

#Las estructuras de datos en Python nos brindan una gran flexibilidad y potencia para almacenar y manipular datos en nuestros programas. 
#Las listas son útiles para colecciones ordenadas y mutables, las tuplas para colecciones ordenadas e inmutables, 
#los diccionarios para almacenar pares clave-valor y los conjuntos para colecciones no ordenadas de elementos únicos.