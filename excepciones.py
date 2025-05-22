#El manejo de excepciones nos permite capturar y manejar errores de manera controlada utilizando las declaraciones try, except y opcionalmente finally.
#La declaración try se utiliza para envolver el código que puede generar una excepción.
#La declaración except se utiliza para capturar y manejar la excepción generada en el bloque try.
#La declaración finally se ejecuta siempre, independientemente de si se generó una excepción o no.

#TRY
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")

#EXCEPT
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

#FINALLY
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción