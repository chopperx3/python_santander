#Python nos permite leer y escribir datos en archivos externos. 
#Podemos abrir archivos en diferentes modos, como lectura ("r"), escritura ("w") o anexar ("a"), y realizar operaciones de lectura y escritura.

#LECTURA DE ARCHIVOS
#El modo "r" se utiliza para leer el contenido de un archivo.

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()


#ESCRITURA EN ARCHIVOS
#El modo "w" sobrescribe el contenido del archivo, mientras que el modo "a" agrega contenido al final del archivo existente.
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()