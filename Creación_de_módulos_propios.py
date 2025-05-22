import mi_modulo

mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

resultado = mi_modulo.sumar(5, 3)
mi_modulo.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = mi_modulo.obtener_nombre_usuario()
mi_modulo.imprimir_mensaje(f"Hola, {nombre}!")