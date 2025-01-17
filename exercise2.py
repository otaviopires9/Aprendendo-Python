# Exercises 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: ")) #INT, para comprar apenas quantidades inteiras
total = quantity * price

print (f"you have bought {quantity} x {item}/S")
print (f"Your total is: ${total}")