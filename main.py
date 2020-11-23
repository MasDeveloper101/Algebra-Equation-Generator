import random
import FlashMail
from passwords import K

operators = ["+", "-", "*", "/"]
plusminus = ["+", "-"]
variables = ["a", "b", "c","d","f","g","h","j","l","m","n","p","q","r","s","t","u","v","x","y","z",]

def RandFormatLvl1():
  randVar = random.choice(variables)
  randnum1 = int(random.randint(1,10))
  randnum2 = int(random.randint(1,10))
  scheme1 = (str(randnum1) + str(randVar) + " = " + str(randnum2))
  scheme2 = (str(randnum2) + " = " + str(randnum1) + str(randVar))
  schemes = [scheme1, scheme2]
  randScheme = random.choice(schemes)
  return(randScheme)

def RandFormatLvl2():
  randVar = random.choice(variables)
  randOp = random.choice(operators)
  randnum1 = int(random.randint(1,10))
  randnum2 = int(random.randint(1,10))
  randnum3 = int(random.randint(1,10))
  scheme1 = (str(randnum1) + str(randVar) +  " " + randOp + " " + str(randnum3) + " = " + str(randnum2))
  scheme2 = (str(randnum2) + " = " + str(randnum1) + str(randVar) +  " " + randOp + " " + str(randnum3))
  schemes = [scheme1, scheme2]
  randScheme = random.choice(schemes)
  return(randScheme)

def RandFormatLvl3():
  randVar = random.choice(variables)
  randOp = random.choice(operators)
  randnum1 = int(random.randint(1,10))
  randnum2 = int(random.randint(1,10))
  randnum3 = int(random.randint(1,10))
  randnum4 = int(random.randint(1,10))
  scheme1 = (str(randnum1) + str(randVar) +  " " + randOp + " " + str(randnum3) + " = " + str(randnum2) +  " " + randOp + " " + str(randnum4) + str(randVar))
  return(scheme1)

def RandFormatLvl4():
  randOp = random.choice(plusminus)
  randOp2 = random.choice(plusminus)
  randnum1 = int(random.randint(1,10))
  randnum2 = int(random.randint(1,10))
  randnum3 = int(random.randint(1,10))
  scheme1 = ("x² " + randOp + " " + str(randnum1) + "x " + randOp2 + " " + str(randnum2) + " = 0")
  scheme2 = (str(randnum3) + "x² " + randOp + " " + str(randnum1) + "x " + randOp2 + " " + str(randnum2) + " = 0")
  scheme3 = ("x² = " + str( ) + "x " + randOp + " " + str(randnum2))
  scheme4 = (str(randnum1) + "(x² " + randOp + " " + str(randnum2) + "x) = " + str(randnum3))
  scheme5 = ("x(x " + randOp + " " + str(randnum1) + ") = " + str(randnum2))
  scheme6 = ("x² " + randOp + " " + str(randnum2) + "x = 0")
  schemes = [scheme1, scheme2, scheme3, scheme4, scheme5, scheme6]
  randScheme = random.choice(schemes)
  return(randScheme)

def main():
  print("||======|| Random Algebra Equation Generator ||======||")
  print("\nChoose a level of equation.")
  print("  1: Level 1 || Example: 2x = 4")
  print("  2: Level 2 || Example: 4x * 9 = 10")
  print("  3: Level 3 || Example: 6x + 2 = 6 + 9x")
  print("  4: Level 4 || Quadratic Equations")
  #levelchoice = input("Enter by Number: ")
  #idx = int(input("\nEnter number of equations: "))
  idx = 10

  levelchoice = "1"

  
  send_to_mail = K.my_email
  yours = K.my_email # The same email in which you enabled less secure app accees
  password = K.my_password
  subject = "Vishwa program"
  message = ""

  if (levelchoice == "1"):
    for x in range(0, idx):
      print("\n" + RandFormatLvl1())
      message += f"{RandFormatLvl1()}\n"
  elif (levelchoice == "2"):
    for x in range(0, idx):
      print("\n" + RandFormatLvl2())
      message += RandFormatLvl2()
  elif (levelchoice == "3"):
    for x in range(0, idx):
      print("\n" + RandFormatLvl3())
      message += RandFormatLvl3()
  elif (levelchoice == "4"):
    for x in range(0, idx):
      print("\n" + RandFormatLvl4())
      message += RandFormatLvl4()
  else:
    print("Error, Program Terminated")

  print("\n\nNow Solve Them\n\nMade by Vishwa Anand")
  FlashMail.send_email(send_to_mail, yours, password, subject, message)

if __name__ == "__main__":
  main()
