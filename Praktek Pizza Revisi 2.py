print ("===WELCOME TO INTERNATIONAL PIZZA HUT DELIVERY===\n")
print (""" Group Name: 
       1. HANSON PHILIP (24091397034)
       2. ADAM NIRVANA (24091397089)
       3. CESYA AULIA RAMADHANI (24091397121)
""")

# Pizza menu with prices for each size
pizza_menu = {
    "Frankfurter BBQ": {"Personal": 50000, "Medium": 93000, "Large": 130000},
    "Meat Monsta": {"Personal": 55000, "Medium": 95000, "Large": 135000},
    "Super Supreme": {"Personal": 60000, "Medium": 100000, "Large": 140000},
    "Super Supreme Chicken": {"Personal": 57000, "Medium": 97000, "Large": 137000},
    "Meat Lovers": {"Personal": 53000, "Medium": 92000, "Large": 132000},
    "Chicken Lovers": {"Personal": 52000, "Medium": 91000, "Large": 128000},
    "Cheese Lovers": {"Personal": 51000, "Medium": 90000, "Large": 125000},
    "American Favourite": {"Personal": 58000, "Medium": 94000, "Large": 132000}
}

# Crust options (additional price for each type of crust)
crust_menu = {
    "Crown Crust": 15000,
    "Stuffed Crust": 12000,
    "PAN Pizza": 0,  # No extra charge
    "Cheesy Bites": 18000
}

# Extra cheese price
extra_cheese_price = 13000

# Taking input from the user
print("1. Topping")
topping = input("""    Frankfurter BBQ
    Meat Monsta
    Super Supreme
    Super Supreme Chicken
    Meat Lovers
    Chicken Lovers
    Cheese Lovers
    American Favourite
                
Choose which topping you want : """)

print("2. Crust")
crust = input("""    Crown Crust
    Stuffed Crust
    PAN Pizza
    Cheesy Bites

Choose which crust you want : """)

print("3. Pizza Size")
size = input(" Personal, Medium, Large : ")

print("4. Extra Cheese? +13000") 
extra_cheese = input("(Yes/No): ")

# Get base price from menu
base_price = pizza_menu.get(topping, {}).get(size, 0)

# Add price for the crust
crust_price = crust_menu.get(crust, 0)

# Add extra cheese price if the user selects it
if extra_cheese.lower() == "yes":
    total_price = base_price + crust_price + extra_cheese_price
else:
    total_price = base_price + crust_price

# Output the final bill
print("Thank you for choosing Pizza Hut Deliveries!")
print(f"Your final bill is: Rp. {total_price}")

