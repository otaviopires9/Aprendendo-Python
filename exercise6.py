import math

#  Econtrar a hipotenusa de um triângulo retângulo

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
result = pow(a, 2) + pow(b, 2)
square = math.sqrt(result)

print(f"The value of the hypotenuse is: {round(square, 2)}cm")

# Depois de terminar o código anterior, percebi que poderia encurta-lo!

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
result = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C is = {round(result, 2)}")