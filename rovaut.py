print("Hello welcome to Rob's Café")

name = input("Whats your name?\n ")

if name == "Saranya" or name == "Ananya" or name == "Ayaan" or name == "Bhavisha" or name == "Maira" or name == "Dev" or name == "Patel" :
    evil_status = input("Are you BAD?\n")
    fan_thoughts = input("How many people have you shown kindness too?\n")
    if evil_status == "Yes" and fan_thoughts == "1" or fan_thoughts == "2" or fan_thoughts == "0" :
        print("You are not welcome here you evil demon, get out")
        exit()
    else:
        print("Oh, so your one of those " + name + " good guys, come on in.")
else:
    print("Hello " + name + ", thank you for coming in today.\n\n\n")
    
menu= "Espresso, Cappuccino, Latte, Cupcake, Tea, Pie, Frappuccino"
print(name + ",what would you like from our menu? Here is what we are serving.\n" + menu )


order = input()

price = 8
 
if order == "Frappuccino":
    price = 10
elif order == "Cappuccino":
    price = 9
elif order == "Tea":
    price = 5
elif order == "Latte":
    price = 15
elif order == "Espresso":
    price = 11
elif order == "Cupcake":
    price = 8
elif order == "Pie":
    price = 60
elif order == "Water":
    price = 0
else:
    print("Sorry we don't have that here.")
    exit()
 
    

quantity = input("How many " + order + ",would you like?\n ")

total = price * int(quantity)


print("Oh, that will be ₹" + str(total) )

print("sounds good " + name + ", we'll have your " + order + " ready for you in a moment")

print("\n Thank you for your order, please visit again")
    


