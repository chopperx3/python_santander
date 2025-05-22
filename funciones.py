#Las funciones son bloques de código reutilizables que nos permiten encapsular tareas específicas y ejecutarlas cuando sea necesario. 
#Las funciones nos ayudan a organizar nuestro código, evitar la repetición y hacer que nuestros programas sean más modulares y fáciles de mantener.
# En Python, definimos una función utilizando la palabra clave def, seguida del nombre de la función y paréntesis que pueden contener parámetros opcionales.

# DEFINICION Y LLAMADA A UNA FUNCION
def saludo():
    print("¡Hola, mundo!")
# Llamamos a la función saludo() para ejecutar el bloque de código que imprime "¡Hola, mundo!"
saludo()  # Imprime "¡Hola, mundo!"

# PARAMETROS Y ARGUMENTOS
def saludo(nombre):
    print(f"¡Hola, {nombre}!")
saludo("Juan")  # Imprime "¡Hola, Juan!"
saludo("María")  # Imprime "¡Hola, María!"

# VALORES DE RETORNO
def suma(a, b):
    return a + b
resultado = suma(3, 4)
print(resultado)  # Imprime 7

# FUNCIONES ANONIMAS
# Las funciones anónimas, también conocidas como funciones lambda, son funciones pequeñas y sin nombre que se definen utilizando la palabra clave lambda.
# Estas funciones son útiles para tareas simples y se utilizan comúnmente en expresiones de una sola línea.
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

# ALCANCE DE LAS VARIABLES
def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función
variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
#print(variable_local)  # Genera un error, la variable no está definida en este alcance.

# DOCUMENTACION DE FUNCIONES

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return print(base * altura)
area_rectangulo(10, 5)  # Imprime 50

# FUNCIONES CON NUMERO VARIABLE DE ARGUMENTOS

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22

#Las funciones son una herramienta fundamental en la programación y nos permiten estructurar y modularizar nuestro código. 
#Con la capacidad de definir funciones personalizadas, podemos encapsular tareas específicas y reutilizarlas en diferentes partes de nuestro programa.