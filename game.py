print("""▄▄   ▄▄▄               ██        ▄▄▄▄                ▄▄▄▄
 ██  ██▀                ▀▀       ██▀▀▀              ██▀▀▀▀█
 ██▄██      ▄█████▄   ████     ███████             ██         ▄█████▄  ████▄██▄
 █████      ▀ ▄▄▄██     ██       ██                ██  ▄▄▄▄   ▀ ▄▄▄██  ██ ██ ██
 ██  ██▄   ▄██▀▀▀██     ██       ██                ██  ▀▀██  ▄██▀▀▀██  ██ ██ ██
 ██   ██▄  ██▄▄▄███  ▄▄▄██▄▄▄    ██                 ██▄▄▄██  ██▄▄▄███  ██ ██ ██
 ▀▀    ▀▀   ▀▀▀▀ ▀▀  ▀▀▀▀▀▀▀▀    ▀▀                   ▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀ ▀▀ ▀▀
   ████▄   ▄▄█████▄
 ██▄▄▄▄██  ██▄▄▄▄ ▀
 ██▀▀▀▀▀▀   ▀▀▀▀██▄
 ▀██▄▄▄▄█  █▄▄▄▄▄██
   ▀▀▀▀▀    ▀▀▀▀▀▀""")



import sys
import random 

print("Welcome to the guessnum")
 
name=input("what is your name?  :-     ")

while name =="":
 name=input(" Please enter what is your name?  :-   ")
else:
 age=(input(f"Hello {name}, what is your age?  :-  "))

if age=="":
 age=input(" Please enter your age :- ")

if age=="":
 print("Invalid age, Try again :) ")
 sys.exit()

choice=input(f"Hello {name}, would you like to play the game? (y/n)  ")
correct=0

while choice=="y":
 number=int(random.randint(1,3))
 guess=int(input("Please input your guess numbers between 1 to 3 (including 1 and 3) :- "))
 if guess==number:
  print("You guessed it right 👍")
  correct+=1
 
 else:
  print(f"your guess is {guess} and programs guess is {number}   You lost 😝😝")
 

 choice=input(f"Hello {name}, would you like to continue the game? (y/n) ")
   


else:
 print(f"Your score is {correct}")
 print (f"{name} tu akta gandu chal nikal bsdk😜")
