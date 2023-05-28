import random

options = ("Piedra", "Papel", "Tijera")
wints_computer=0
wints_user=0
rounds = 1

while True:

  print("*"*20)
  print("Rout", rounds)
  print("*"*20)

  print("Puntos PC", wints_computer)
  print("Puntos User", wints_user)
  
  user_option = input("Escoge Piedra, Papel o Tijera--> ").capitalize()
  print("User option-->", user_option)
  rounds +=1
  
  if not user_option in options:
    print("Elección incorrecta")
    continue
    
  computador = random.choice(options)
  print("Computer option-->", computador)
  
  if user_option == computador:
    print("Empate")
  elif user_option == "Piedra":
    if computador == "Tigera":
      print("Piedra gana a Tijera")
      print("User gana")
      wints_user +=1
    else:
      print("Papel gana a Piedra")
      print("PC gana")
      wints_computer +=1
  elif user_option == "Papel":
    if computador == "Piedra":
      print("Papel gana a Piedra")
      print("User gana")
      wints_user +=1
    else:
      print("Tijera gana a Papel")
      print("PC gana")
      wints_computer +=1
  elif user_option == "Tijera":
    if computador == "Papel":
      print("Tijera gana a Papel")
      print("User gana")
      wints_user +=1
    else:
      print("Piedra gana a Tijera")
      print("PC gana")
      wints_computer +=1

  if wints_computer ==2:
      print("El ganador es la computadora")
      break
  if wints_user ==2:
      print("El ganador es el ususario")
      break
      

