# input() = Uma função que pede ao usuário para inserir dados
#           E devolve os dados como uma string

name = input("What is your name?: ")
age = int(input("How old are you?: ")) # Para converter uma variável INPUT, temos que colocar antes do mesmo(input)

age = age + 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old!")

print(type(age))