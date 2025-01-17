import math

# Calcule a área de um círculo   A = πr²

radius = float(input("Enter the radius of the circle: "))

area = math.pi * pow(radius, 2) #usar função pow() que faz uma potência
print(f"The area of the circumference is: {round(area, 2)}cm^2")
