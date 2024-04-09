
# Ghost Game in Python

from random import randint
from tkinter import NO, YES
ghost_door = object


print("******************************")
print("******************************")
print("********* JUEGO DEL FANTASMA :)*********")
print("******************************")
print("******************************")
print()
print("******************************")
print("***** VARIAS PUERTAS  *****")
print("******************************")
print()
print("******************************")
print("HAY UN FANTASMA DETRAS DE ESAS PUERTAS")
print("******************************")
print("******************************")
print("ELIGE UN NUMERO DE PUERTA \n  HASTA LLEGAR A 15 PUNTOS O APAREZCA EL FANTASMA  \n\n CADA PUERTA SIN FANTASMA\n   TE DA 5 PUNTOS")
print("******************************\n")
print ("PARA ACABAR EL JUEGO NECESITAS 50 PUNTOS")

score = 0
doors = 3
ghost_count = 1
level = 1 

level_choose = input ("Nivel 1 / Nivel 2 / Nivel 3 / Dificil")
if level_choose == "Nivel 1":

 while score < 30:
    ghost_door = randint (1,doors)
    door_choosen = int(input(f"QUE PUERTA DEL 1 AL {doors}? "))
    
    if ghost_door == door_choosen:
        print("\nFANTASMA! FANTASMA!! FANTASMA!!!")
        print ("HAS PERDIDO LA PARTIDA!")

           
        break
    else:
        print("HAS GANADO 5 PUNTOS :)")
        score += 5
       
 if score > 10:
    doors = 4 
 if score > 20:
    doors = 5
    ghost_count = 2

if level_choose == "Nivel 2":
    print ("Bienvenido al Nivel 2 ")
    score == 31


if score == 30:
    print ("Enhorabuena has ganado la partida")
    print ("Deseas continuar?")
    game_choose = input("YES / NO")
    if game_choose == "YES":
        score += 1 
    
    if game_choose == "NO":
        print ("Enhorabuena has ganado el Nivel 1")
        print ("Tu puntuacion = score")

while score >= 31:
    level += 1 
    doors = 5
    ghost_count = 2
    print ("Nivel 2")
    ghost_door = randint (1,doors)
    door_choosen = int(input(f"QUE PUERTA ELIGES DEL 1 AL {doors}? "))
    if ghost_door == door_choosen:
        print("\nFANTASMA! FANTASMA!! FANTASMA!!!")
        score == 50
        break
    else:
        print("HAS GANADO 5 PUNTOS :)")
        score += 5
        doors += 1


if level_choose == "Dificil":
   level += 10000
   doors = 2
   print ("Bienvenido al nivel más complicado")
   ghost_door = randint (1,doors)
   door_choosen = int(input(f"ELIGE UNA PUERTA ENTRE 1 Y {doors}"))
   if ghost_door == door_choosen:
        print("\nFANTASMA! FANTASMA!! FANTASMA!!!")
        score == 50
   else:
        print("HAS GANADO EL NIVEL MÁS COMPLEJO:)")
        score += 1000
    
    

if score >= 50:
 print("\n TU PUNTUACIÓN SCORE =", score)
 print ("Game made by thehlb100")
 print ("V2.0 Date: 12/1/2024" )