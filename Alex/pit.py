import keyword

import random

def decrypt_clue():
  file = open("mysterious.txt", "r")

  data = file.read()

  keywords_list = keyword.kwlist

  list_data = []

  for word in keywords_list:
    if word in data:
      list_data.append(word)

  return list_data

def solve_puzzles():
  list_data = []

  file = open("puzzles.txt", "r")

  data_list = file.read().splitlines()

  for item in data_list:
    if(item):
      list_data.append(True)

    else:
      list_data.append(False)

  return list_data

def calculate_magic_numbers(start, end):
  sum = 0

  list_magic = []

  for number in range(start, end):

    while (number > 0 or sum > 9):

        if (number == 0):
          number = sum
          sum = 0

        sum = sum + number % 10

        number = int(number / 10)

    list_magic.append("yes") if (sum == 1) else list_magic.append("no")

  return list_magic

def exam_numbers():

  for i in range(5):
  
    number = random.getrandbits(4)
    
    input_data = int(input(f"what is decimal number of {bin(number)[2:]} : "))
    
    if(input_data == number):
      print("it's true")
      
    else:
      print("it's false")

list_words = decrypt_clue()

list_values = solve_puzzles()

start = int(input("enter start period number of magic number creation : "))
end = int(input("enter end period number of magic number creation : "))

list_magic = calculate_magic_numbers(start, end)

exam_numbers()
