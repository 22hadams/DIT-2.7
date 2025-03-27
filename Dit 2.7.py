Pizza_Matarial =[["Bases","Wholegrain", "Normal"],
["Sauces","Normal Tomato", "Tomato with herbs"],["Cheese","Colby","Mozzeralla","Parmasiano"],
["Toppings","Onions","Peparoni","Proccieto"],["Drinks","Lemonade","Cola","Beer"],["Sides","Fries","Popcorn Chicken"]
]
Q_Cycle = 0
Choice = 0
def Question_Cycle():
    global Q_Cycle
    print("Choose your", (Pizza_Matarial[Q_Cycle][0])+"?")

    for i in range (1,len(Pizza_Matarial[Q_Cycle])):
        input(f"{i} = {(Pizza_Matarial[Q_Cycle][i])}")
    Q_Cycle +=1




def Store_Answer():
    global Q_Cycle
    global Choice
    



while Q_Cycle < len(Pizza_Matarial):
    Question_Cycle()



