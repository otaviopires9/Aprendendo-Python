# Variable = Guarda um valor (string, integer, float, boolean)
#          = Uma variável se comporta conforme o valor que contém

# Como utilizar Stings (USADAS PARA REPRESENTAR TEXTOS!) 

first_name = "Otávio"
print (f"Hello {first_name}")
# Usar (f) é a maneira mais fácil de exibir uma variável!
# Digita (f) fora do conjunto de aspas, assim: print(f"mensagem ")
# Para fazer o (f) funcionar com a variável, você precisa de um conjunto de chaves {como esses}
# Ficando assim: print(f"mensagem {nome da variável}")

food = "pizza"
print (f"Você gosta de {food}?")

email = "gocallaita123@fake.com"
print (f"Seu email é: {email}")

# Como utilizar Integers (São números inteiros)
# Pode ser a idade, quantidade, 
# NÃO DEVEM ESTAR ENTRE ASPAS(porque seria uma STRING tecnicamente)
age = 18
print (f"Eu tenho {age} anos")
quantity = 3 
print (f"Você tem {quantity} peixes nas mãos")
num_students = 9
print (f"Existem {num_students} estudantes na sua sala de aula")

# Como utilizar Floats (Que são números que contenham uma parte decimal)
# Temos como exemplo preço, médiam, distância
price = 9.99
print (f"O preço é ${price}")

gpa = 5.3
print (f"Sua média é: {gpa}")

distance = 6.9
print (f"Você correu {distance}km")

# Como utilizar boolean (boolean é verdeiro ou falso)
# Boolean é apenas True (verdadeiro) ou False (false)
# True e False, necessariamente tem que iniciar com letra maiúscula

is_student = True
print (f"Você é um estudante?: {is_student}")

a_dog = False
if a_dog:
    print ("Eu sou um cachorro!")
else:
    print ("Eu não sou um cachorro!")

for_sell = False
if for_sell: #NÃO ESQUECER DOS DOIS PONTOS AQUI!!!
    print ("Sim, este item está à venda!")
else:
    print ("Não, este item não está à venda")


#Usando todas as variáveis!
user_name = "tesouro"
year = 2025
pi = 3.14
is_admin = True
if is_admin:
    print ("Sim, sou adm!")
else:
    print ("Não, não sou adm!")

    #É O TESOURO NÉ VIDA