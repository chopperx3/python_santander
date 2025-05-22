#Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. 
#Los elementos de una tupla se encierran entre paréntesis (), separados por comas.

punto = (3, 4)

print(punto[0])  # Imprime 3
print(punto[1])  # Imprime 4

# Las tuplas pueden contener diferentes tipos de datos, incluyendo números, cadenas y otras tuplas.

tupla_mixta = (1, "hola", 3.14, (2, 3))
print(tupla_mixta[1])  # Imprime "hola"
print(tupla_mixta[3])  # Imprime (2, 3)
print(tupla_mixta[3][0])  # Imprime 2

#count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
#index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
#len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.

mi_tupla = (1, 2, 3, 2, 4, 2)

print (mi_tupla.index(2))   # Salida: 1
print (mi_tupla.index(2, 2))   #Salida: 3
print (mi_tupla.index(2, 2, 4))   #Salida: 3


# Las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas.


#Las estructuras de datos en Python nos brindan una gran flexibilidad y potencia para almacenar y manipular datos en nuestros programas. 
#Las listas son útiles para colecciones ordenadas y mutables, las tuplas para colecciones ordenadas e inmutables, 
#los diccionarios para almacenar pares clave-valor y los conjuntos para colecciones no ordenadas de elementos únicos.