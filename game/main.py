import random

print("""
  [ 🤖 Bienvenido al juego Piedra, Papel o tijera  🙋 ]
            >>> Ingresa una opción <<<
            
      """)

def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input(">>> Piedra, papel o tijera => ").lower()

  if not user_option in options:
    print("Esa opción no es validad")
    #continue
    return None, None

  computer_option = random.choice(options)  #Computador escoge igual que el usuario(las mismas opciones)

  print("User option => ", user_option)
  print("Computer option => ", computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
     print("Empate!\n")
  elif user_option == "piedra":
      if computer_option == "tijera":
         print("🪨 Piedra gana a tijera ✂️")
         print("¡User gana!\n")
         user_wins += 1
      else:
          print("📄 Papel gana a piedra 🪨")
          print("¡Computer gana!\n")
          computer_wins += 1
  elif user_option == "papel":
      if computer_option == "piedra":
          print("📄 Papel gana a piedra 🪨")
          print("¡User gana!\n")
          user_wins += 1
      else:  
          print("✂️ Tijera gana a papel 📄")
          print("Computer gana!\n")
          computer_wins += 1
  elif user_option == "tijera": 
      if computer_option == "papel":
         print("✂️ Tijera gana a papel 📄")
         print("¡User gana!\n")
         user_wins += 1
      else:
          print("🪨 Piedra gana a tijera ✂️")
          print("¡Computer gana!\n")
          computer_wins += 1

  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):

  print(f"""
  🤖 Computer wins: {computer_wins}
  🙋 User wins: {user_wins}
         """)

  if user_wins == 3:
     print("🎖️ El ganador es User 🎖️")
     exit()

  if computer_wins == 3:
     print("🎖️ El ganador es Computer 🎖️")
     exit()

def run_game():

    computer_wins = 0
    user_wins = 0
    rounds = 1


    while True :
       print("***" * 10)
       print("Round", rounds)
       print("***" * 10)

       rounds += 1


       user_option, computer_option = choose_options()
       user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
       check_winner(user_wins, computer_wins)

run_game()