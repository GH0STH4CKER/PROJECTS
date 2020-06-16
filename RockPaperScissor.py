import random , string , time , sys
from colorama import Fore, init
init()
print(Fore.LIGHTGREEN_EX + " ______           _   ______                     _____      _                      ")
print(" | ___ \         | |  | ___ \                   /  ___|    (_)                     ")
print(" | |_/ /___   ___| | _| |_/ /_ _ _ __   ___ _ __\ `--.  ___ _ ___ ___  ___  _ __   ")
print(" |    // _ \ / __| |/ /  __/ _` | '_ \ / _ \ '__|`--. \/ __| / __/ __|/ _ \| '__|  ")
print(" | |\ \ (_) | (__|   <| | | (_| | |_) |  __/ |  /\__/ / (__| \__ \__ \ (_) | |     ")
print(" \_| \_\___/ \___|_|\_\_|  \__,_| .__/ \___|_|  \____/ \___|_|___/___/\___/|_|     ")
print("                                | |                                                ")
print("                                |_|   @GHO$TH4CKER ")
print(Fore.LIGHTYELLOW_EX + "--------------------------------------------------------------------------------------\n")

def slowprint(str):
   for c in str :
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.05)

print("r = Rock   p = Paper   s = Scissor")
A,B = 0,0
print(Fore.LIGHTGREEN_EX + "")
name = input(" What is your name : ")
print("")
slowprint(" Hi ")
slowprint(name)
slowprint(" ! Let's start the game")
print("")

for x in range(5):
  print(Fore.LIGHTGREEN_EX + "")
  usr = input("Player (r/p/s) : ")
  time.sleep(0.5)
  usr.lower()

  while True:
      bot = random.choice(string.ascii_letters)
      if bot == "r" or bot == "p" or bot == "s" :
        break
  print("Computer       :",bot)
  time.sleep(0.6)

  if usr == "r" and bot == "p":
      print(Fore.LIGHTRED_EX + "computer won")
      B += 1
  elif usr == "r" and bot == "s":
      print(Fore.LIGHTGREEN_EX + "you won")
      A += 1
  elif usr == "p" and bot == "r":
      print(Fore.LIGHTGREEN_EX + "you won")  
      A += 1
  elif usr == "p" and bot == "s":
      print(Fore.LIGHTRED_EX + "computer won")  
      B += 1
  elif usr == "s" and bot == "p":
      print(Fore.LIGHTGREEN_EX + "you won")
      A += 1     
  elif usr == "s" and bot == "r":
      print(Fore.LIGHTRED_EX + "computer won")
      B += 1
  elif usr == bot:
      print("Round Tied") 
  else:
      print("invalid input")  
  print(Fore.LIGHTCYAN_EX + "              SCORE                  ")                       
  print("Player ",A,"------------",B," Computer")
  time.sleep(0.4)    

if A > B :
    time.sleep(0.4)
    print("\n---Congratulations",name,"---")
    print(Fore.LIGHTGREEN_EX + "*** YOU WON THE GAME ***")
elif B > A :
    time.sleep(0.4)
    print(Fore.LIGHTRED_EX + "\n!!! COMPUTER WON THE GME !!!")
else:
    time.sleep(0.4)
    print(Fore.LIGHTYELLOW_EX + "\n??? THE GAME TIED ???") 

time.sleep(1)
input("\n\nExit >")
