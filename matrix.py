import os, time, random, colorama
from colorama import Fore, Back, Style, init
init()

a = random.randint(1,9)
print(Fore.LIGHTGREEN_EX)    

while True:

  for x in range(9):
    print(a, end =" ") 
    a = random.randint(1,9)

  time.sleep(0.01)


#THIS IS MATRIX RAIN PROGRAM