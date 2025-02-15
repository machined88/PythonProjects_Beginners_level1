#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pwd_letters = ""
pwd_sym =""
pwd_num = ""
for a in range(1,nr_letters+1):
 pwd_letters = pwd_letters + random.choice(letters)
for a in range(1,nr_numbers+1):
 pwd_num = pwd_num + random.choice(numbers)
for a in range(1,nr_symbols+1):
 pwd_sym = pwd_sym + random.choice(symbols)
print("Congratulations, your password is successfully created")
print(f"Easy one : {pwd_letters+pwd_num+pwd_sym}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = pwd_letters+pwd_num+pwd_sym
count = len(password)
pass_list = []
for i in range(0,count):
 pass_list.append(password[i]);
hard_pwd=""
count1 = len(pass_list)
for i in range(count1):
  str = random.choice(pass_list)
  hard_pwd = hard_pwd + str
  pass_list.remove(str)
print(f"Hard one : {hard_pwd} ")
