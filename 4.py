def Cel_TO_Fo(input_data):
    result = float(((18 / 10) * input_data) + 32)
    
    return result

def Fo_TO_Cel(input_data):
    result = float(((input_data - 32) * 10) / 18)
    
    return result

option = int(input("[1] celcius to fahreneit \n [2] fohreneit to celcius \n enter option : "))

data = int(input("enter number : "))

if(option == 1):
    result = Cel_TO_Fo(data)
    
    print(f"\n Result : {result}")
    
elif(option == 2):
    result = Fo_TO_Cel(data)
    
    print(f"\nResult : {result}")
    
else:
    print("wrong option you choose")