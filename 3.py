def Sum(number1, number2):
    result = number1 + number2
    
    return result

def Multiple(number1, number2):
    result = number1 * number2
    
    return result

def Divide(number1, number2):
    result = number1 / number2
    
    return result

def Difference(number1, number2):
    if(number1 > number2):
        result = "big"
        
    elif(number1 < number2):
        result = "low"
        
    else:
        result = "no"
        
    
    return result

option = int(input("[1] sum \n [2] multiple \n [3] divide \n [4] difference \n enter option : "))

number1 = int(input("Enter number one : "))
number2 = int(input("Enter number two : "))

result = 0

if(option == 1):
    result = Sum(number1, number2)
    print(f"\nResult of Sum is : {result}")
    
elif(option == 2):
    result = Multiple(number1, number2)
    print(f"\nResult of Multiple is : {result}")
    
elif(option == 3):
    result = Divide(number1, number2)
    print(f"\nResult of Divide is : {result}")
    
elif(option == 4):
    result = Difference(number1, number2)
    
    if(result == "big"):
        print(f"\n {number1} is bigger than {number2}")
        
    elif(result == "low"):
        print(f"\n {number1} is lower than {number2}")
        
    else:
        print(f"\n {number1} and {number2} are equal")