# Exercise 1 Rectangle Area Calc(calcular a area de um retângulo)
#          Área = lenght x weight  
#          Pedir para o usuário inserir o valor da altura e da largura!

lenght = float(input("Enter height value!: ")) #Lembrar de colocar FLOAT or INT antes do input, para converter a string para integer(Para poder utilizar operações aritiméticas)
width = float(input("Enter width value!: "))
area = lenght * width

print(f"The area is: {area}cm ")