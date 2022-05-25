import random
#Getting the Users Name
print("Welcome To Romeo's Maori Quiz")
print("You Will Be Given Maori Numbers, Please Answer these in English")
print("Please Enter The Following Questions To Start The Game")
def get_name():
    name_local = input("What is your name?: ")
    return name_local

def get_age():
    age_local = input("Whats your age?: ")
    return age_local
score = 0

name = get_name() #1st Function
age = get_age() #2nd Function
difficulty = input("Easy or Hard? H or E: ").upper()
print(f"\nHi {name} . At {age} years old, hope you find this fun.\n"  
      "\nAnyway, this is a test about numbers in moari to english.\n"
      "You will need to enter the following number in english which applies to"
      " the maori number  e.g Tekau mā Tahi = 11 \n")
print("Your current score is",score)
if difficulty == "H":
    numbers = [["Tekau mā Tahi", 11], ["Tekau mā Rua", 12], ["Tekau mā Toru", 13], ["Tekau mā Wha", 14],
               ["Tekau mā Rima", 15], ["Tekau mā Ono", 16], ["Tekau mā Whitu", 17], ["Tekau mā Waru", 18],
               ["Tekau mā Iwa", 19], ["Rua Tekau", 20]]
    random.shuffle(numbers)
else:
    numbers = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Wha",4],["Rima",5],
               ["Ono", 6],["Whitu",7],["Waru", 8],["Iwa", 9],["Tekau", 10]]
    random.shuffle(numbers)

for i in numbers:
      answer = int (input(f"Please Enter the Following Number In English ,  {i[0]}:"))
      if answer == i[1]:
          print("###### CORRECT! ######\n")
          score = score+1
          print("Your Current Score Is",score)
      else:
          print("XXXXX INCORRECCT! XXXXX\n")
          score = score-1
          print("Your Current Score Is",score)

print("Well done You Have Finished With A Score Of",score)

