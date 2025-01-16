# Variable = Guarda um valor (string, integer, float, boolean)
#          = Uma variável se comporta conforme o valor que contém

# Como utilizar Stings (USADAS PARA REPRESENTAR TEXTOS!) 

primeiro_nome = "Otávio"
print (f"Olá {primeiro_nome}")
# Usar (f) é a maneira mais fácil de exibir uma variável!
# Digita (f) fora do conjunto de aspas, assim: print(f"mensagem ")
# Para fazer o (f) funcionar com a variável, você precisa de um conjunto de chaves {como esses}
# Ficando assim: print(f"mensagem {nome da variável}")

comida = "pizza"
print (f"Você gosta de {comida}?")

email = "gocallaita123@fake.com"
print (f"Seu email é: {email}")

# Como utilizar Integers (São números inteiros)
# Pode ser a idade, quantidade, 
# NÃO DEVEM ESTAR ENTRE ASPAS(porque seria uma STRING tecnicamente)
idade = 18
print (f"Eu tenho {idade} anos")
quantidade = 3 
print (f"Você tem {quantidade} peixes nas mãos")
num_estudantes = 9
print (f"Existem {num_estudantes} estudantes na sua sala de aula")

# Como utilizar Floats (Que são números que contenham uma parte decimal)
# Temos como exemplo preço, médiam, distância
preco = 9.99
print (f"O preço é ${preco}")

media = 5.3
print (f"Sua média é: {media}")

distancia = 6.9
print (f"Você correu {distancia}km")

# Como utilizar boolean (boolean é verdeiro ou falso)
# Boolean é apenas True (verdadeiro) ou False (false)
# True e False, necessariamente tem que iniciar com letra maiúscula

um_estudante = True
print (f"Você é um estudante?: {um_estudante}")

um_cachorro = False
if um_cachorro:
    print ("Eu sou um cachorro!")
else:
    print ("Eu não sou um cachorro!")

para_venda = False
if para_venda: #NÃO ESQUECER DOS DOIS PONTOS AQUI!!!
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