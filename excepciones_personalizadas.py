#Para crear una excepción personalizada, debes crear una clase que herede de la clase base Exception o de una de sus subclases.

def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")

try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")

#Cuando ocurre un error en tu código, Python genera una excepción. Al utilizar bloques try-except, puedes capturar y manejar estas excepciones de manera adecuada. 
#Puedes especificar diferentes bloques except para manejar distintos tipos de excepciones y realizar acciones específicas en cada caso.