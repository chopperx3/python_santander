#Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor. 
#Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. 
#Los diccionarios se encierran entre llaves {}, y los pares clave-valor se separan por comas.

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"

#Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

#clear(): elimina todos los elementos del diccionario.
#copy(): devuelve una copia superficial del diccionario.
#keys(): devuelve una vista de todas las claves del diccionario.
#values(): devuelve una vista de todos los valores del diccionario.
#items(): devuelve una vista de todos los pares clave-valor del diccionario.
#update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

#Las estructuras de datos en Python nos brindan una gran flexibilidad y potencia para almacenar y manipular datos en nuestros programas. 
#Las listas son útiles para colecciones ordenadas y mutables, las tuplas para colecciones ordenadas e inmutables, 
#los diccionarios para almacenar pares clave-valor y los conjuntos para colecciones no ordenadas de elementos únicos.