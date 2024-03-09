import os

option = 1

card_number = 0
Cards_List = []
Mojoodi_List = []

def EnterCard():
    return int(input("Enter your card : "))

def FoundCard(input_data):
    counter = 0
    for item in Cards_List:
        if(item == input_data):
            card_number = counter
            break
        elif(item != input_data):
            counter += 1

    return counter

def Deposit():
    card = EnterCard()
    
    card_number = FoundCard(card)

    cash = int(input("enter amount of cash you want to deposit : "))
    
    Mojoodi_List[card_number] += cash

def Withdraw():
    card = EnterCard()
    
    card_number = FoundCard(card)

    cash = int(input("enter amount of cash you want to withdraw : "))
    
    Mojoodi_List[card_number] -= cash

def AddCard():
    card_input = EnterCard()
    
    number = FoundCard(card_input)
    
    if(number == Cards_List.__len__()):
        Cards_List.append(card_input)
        Mojoodi_List.append(int(input("Enter Amount of your card : ")))
        
    else:
        print("You already add this card to list!!")

def RemoveCard():
    card = EnterCard()
    
    Mojoodi_List.remove(FoundCard(card))
    
    Cards_List.remove(card)

def HowMuch():
    card = EnterCard()
    
    card_number = FoundCard(card)
    
    print("Amount of Cash in Account : " + str(Mojoodi_List[card_number]))
    
    input("\n press enter...")

while option:
    option = int(input("[1] Add Card \n [2] Deposit \n [3] Withdraw \n [4] Remove \n [5] Mojoodi \n [0] exit \n Enter Option :"))
    
    if(option == 0):
        pass
    elif(option == 1):
        AddCard()
    elif(option == 2):
        Deposit()
    elif(option == 3):
        Withdraw()
    elif(option == 4):
        RemoveCard()
    elif(option == 5):
        HowMuch()
    else:
        print("Wrong Option")
    
    os.system('cls')