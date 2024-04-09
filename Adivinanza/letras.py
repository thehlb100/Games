from random import randint
import math

def ahorcado():
 #Elección de palabras a partir de archivo de texto

 #Temática ordenador
 archivoPalabras = open("ordenador.txt", "r")
 palabras = archivoPalabras.read()
 listaPalabras = palabras.split("\n")
 longitudListaPalabras = len(listaPalabras)
 palabraSeleccionada = randint(0, longitudListaPalabras-1)

 #Temática frutas y verduras
 archivoPalabras1 = open('frutas.txt',"r")
 palabras1 = archivoPalabras1.read()
 listaPalabras1= palabras1.split("\n")
 longitudListaPalabras1= len(listaPalabras1)
 palabraSeleccionada1= randint(0,longitudListaPalabras1-1)

 #Inicio
 print ("Bienvenido al juego del ahorcado!!")
 print ("Tienes 10 intentos para adivinar una palabra")
 print ('Qué temática desesas escoger')
 print ('Partes del ordenador (1)')
 print ('Frutas y verduras (2)')

 #Elección de la temática
 NivelElegido = int(input())


 #Juego
 if NivelElegido == 1:
  print ('Que palabra escoges?')
  respuesta = str(input())
  if respuesta == (listaPalabras[palabraSeleccionada]):
    print ("Has ganado")

  else:
   print ('No es correcto')
   print (f'La respuesta correcta era {longitudListaPalabras[palabraSeleccionada]}')

   

 if NivelElegido==2:
  print ('Que palabra escoges?')
  respuesta = str(input())
  if respuesta == (listaPalabras1[palabraSeleccionada1]):
    print('Has ganado!')
  
  else:
    print('La palabra no es correcta')
    print (f'La respuesta correcta era {longitudListaPalabras1[palabraSeleccionada1]}')

  

ahorcado()






