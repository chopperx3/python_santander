#Crear y utilizar módulos personalizados
# #Podemos crear nuestros propios módulos definiendo funciones y variables en un archivo separado y luego importándolo en otros programas.

#mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")


def calcular_suma(a, b):
    return a + b

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


# utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)


def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")