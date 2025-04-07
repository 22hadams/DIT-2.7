
Pizza_Matarial = {
	"Bases": ["Wholegrain", "Normal"],
	"Sauces": ["Normal Tomato", "Tomato with herbs"],
	"Cheese": ["Colby", "Mozzarella", "Parmesan"],
	"Toppings": ["Onions", "Pepperoni", "Prosciutto"]
}
Sides = {
	"Sides": ["Fries", "Popcorn Chicken"]
}
Drinks = {
    "Drinks": ["Lemonade", "Cola", "Beer"]
}
Menu_Options = {
    "Food and Drinks": ["Pizza", "Sides", "Drinks","Complete Order"],
}
custom_pizza = []
sides_order = []
drinks_order = []
Final_Order = []
Mlist = []
def Func_Input_Validation(Ingredients,TList):
    while True:
        Input = input()
        if Input.isdigit():
            index = int(Input) - 1
            if 0 <= index < len(Ingredients):
                if Ingredients[index] in Ingredients:
                    TList.append(Ingredients[index])
                    return True
                else:
                    print("Invalid input, please try again.")
            else: 
                print("Invalid input, please try again.")
        elif Input in Ingredients:
            TList.append(Input)
            return True
        else:
            print("Invalid input, please try again.")
def Question_Custom_Pizza():# Custom Pizza Questions (Outputs a custom Pizza)
    for category, ingredients in Pizza_Matarial.items():
                print(f"What {category} would you prefer?\n")
                print("Options:")
                for i, option in enumerate(ingredients, start=1):
                    print(f"{i}.{option}")
                Func_Input_Validation(ingredients,custom_pizza)
    print("Your custom pizza is:")
    for item in custom_pizza:
        print(item)
    #Final_order(custom_pizza,0,0,0)
    custom_pizza.clear()
    return
def Question_Sides():# Custom side Questions (Outputs a custom side)
    for category, ingredients in Sides.items():
                print(f"What {category} would you prefer?\n")
                print("Options:")
                for i, option in enumerate(ingredients, start=1):
                    print(f"{i}.{option}")
                Func_Input_Validation(ingredients,sides_order)
    print("Your Extra's are:")
    for item in sides_order:
        print(item)
    #Final_order(0,sides_order,0,0)
    sides_order.clear()
    return
def Question_Drinks():# Custom Drink Questions (Outputs a custom Drink)
    for category, ingredients in Drinks.items():
                print(f"What {category} would you prefer?\n")
                print("Options:")
                for i, option in enumerate(ingredients, start=1):
                    print(f"{i}.{option}")
                Func_Input_Validation(ingredients,drinks_order)
    print("Your Extra's are:")
    for item in drinks_order:
        print(item,"\n")
    #Final_order(0,0,drinks_order,0)
    drinks_order.clear()
    return
"""def Final_order(Pizza_order,Sides_order,Drinks_order,End):
    global Final_Order
    while True:
        if Pizza_order:
            print(Pizza_order)
            Final_Order.append(Pizza_order)
            print(Final_Order)
        if Sides_order:
            Final_Order.append(Sides_order)
        if Drinks_order:
            Final_Order.append(Drinks_order)
        if End != 0:
            print("Your order is:")
            print(Final_Order)
            Final_Order.clear()
            return True
        return False   """
def Main():
    while True:
        Mlist.clear()
        for category, ingredients in Menu_Options.items():
                    print("Menu")
                    for i, option in enumerate(ingredients, start=1):
                        print(f"{i}.{option}")
                    Func_Input_Validation(ingredients,Mlist)
                    if Mlist:
                        Mode = Mlist[0]
                        break
                    else:
                        continue
        if Mode == "Pizza":
            Question_Custom_Pizza()
        elif Mode == "Sides":
            Question_Sides()
        elif Mode == "Drinks":
            Question_Drinks()
        else:
            #Final_order(0,0,0,1)
            print("Thank you for your order!")
            print("Unfortunately, our order is down at the moment.")
            Mode = ""
            custom_pizza.clear()
            drinks_order.clear()
            sides_order.clear()
            print("Order Complete!")
            break

print("Welcome to the Pizza Ordering System!")
print("Here we sell Pizza, Sides and Drinks.\n")
print("What would you like to order?\n")
Main()