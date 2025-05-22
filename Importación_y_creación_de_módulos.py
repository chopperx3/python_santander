#En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas. 
#La importación de módulos nos permite acceder a la funcionalidad definida en otros archivos y reutilizar código de manera eficiente. 
#Además, podemos crear nuestros propios módulos para organizar y modularizar nuestro código.

#IMPORTACIÓN DE MÓDULOS
#Python proporciona una amplia variedad de módulos integrados que podemos importar y utilizar en nuestros programas.

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

#También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

#Funciones y clases de módulos estándar
#Python incluye módulos estándar que proporcionan funciones y clases útiles para diversas tareas.
#EJEMPLO DE USO DE MÓDULOS ESTÁNDAR

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10
fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual