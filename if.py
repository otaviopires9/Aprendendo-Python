# if = Executar um código apenas se(if) uma condição for verdadeira(True)
#      else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("OOOMG it's a dinosaur")
elif age >= 18:
    print("Credit Card application accepted!")
elif age < 0:
    print("You haven't even been born yet!")
else:
    print("You must be 18+ to sign up")


response = str(input("Would you like food? (Y/N): "))

if response == "Y": # O == é um operador de comparação, para ver se dois valors são iguais
    print("Have some food!")
else:
    print("No food for you!")

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

online = True

if online:
    print("The user is online")
else:
    print("The user is offline")