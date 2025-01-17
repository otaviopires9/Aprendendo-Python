# Typecasting = é o processo de conversão de uma variável de um tipo de dado para outro.
# Isso permite que você transforme valores de um tipo (como integer, boolean, string ou float) em outro, dependendo das necessidades do programa.
#               str(), int(), float(), bool()

name = "Otávio Pires" # É do tipo (str)
age = 18 # É do tipo (int)
gpa = 9.9 # É do tipo (float)
is_student = True # É do tipo (boolean)

print (type(is_student)) # Para descobrir o tipo de variável

# Converter uma variável

gpa = int(gpa) # Fazendo isso convertemos uma variável float em uma variável int(tirando a parte decimal, ou seja, tiramos a parte quebrada do número)
print(gpa) 

age = float(age) # Fazendo isso convertemos uma variável int em uma variável float(adicinando a parte decimal ao número)
print(age)

name = bool(name) # Ao converter name a uma variável booleana quando deixamos ela vazia, nos é retornado False, já quando temos qualquer coisa digitada, nos retorna True!
print (name)

age = 18
age = str(age)
print (age)
print (type(age)) # Podemos converter uma variável int em str(não podemos usar str(strings) em operações aritiméticas)


# Especiamente útil para entrada de usuário!