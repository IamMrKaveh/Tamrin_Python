data = input("please enter data : ")

int_data = 0

string_data = "0"

flag = True
for item in data:
  try:
    int_data = int(item)
    
  except:
    flag = False
    string_data = str(data)
    break
  
  
if(string_data != "0"):
  print("your input data type is string")
  
else:
  print("your input data type is int")