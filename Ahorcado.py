from random import randint
import math

#Elección de palabras a partir de archivo de texto

archivoPalabras = open("ordenador.txt", "r")
palabras = archivoPalabras.read()
listaPalabras = palabras.split("\n")
longitudListaPalabras = len(listaPalabras)
palabraSeleccionada = randint(0, longitudListaPalabras-1)
intentos = 10

#Juego
def pregunta():
 print ('Que palabra escoges?')
 respuesta = str(input())
 if respuesta == (listaPalabras[palabraSeleccionada]):
    print ("Has ganado")

 else:
   print ('No es correcto')
   intentos-1
   print (f"El número de intentos restantes es de {intentos}")
  
   pregunta()
 if intentos == 0:
   print ("Has perdido")
   print (f'La respuesta correcta era {listaPalabras[palabraSeleccionada]}')

#Inicio
print ("Bienvenido al juego del ahorcado!!")
print ("Tienes 10 intentos para adivinar una palabra")
print ("La palabra está realacionada con la informática")
print ("Que comience el juego!")
pregunta()


print('Game made by TheHlb100')



