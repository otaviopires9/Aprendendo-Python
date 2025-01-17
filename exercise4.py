import math

# Calcular a circunferência de um círculo 
#     formula: C = 2πr

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius  

print(f"The circumference is: {round(circumference, 2)}cm") # Quando colocamos a função round(x, 2) assim, o número após a vírgula determina quantas casas decimais o número vai ter