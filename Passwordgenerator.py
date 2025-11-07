import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
         "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D",
         "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",
         "T","U","V","W","X","Y","Z"]
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=["$","@","!","#","%","^","&","*"]
password_list=[]
print("Welcome to password generator")
nc=int(input("enter no of characters do you want in your password"))
np=int(input("enter no of numbers do you want in your password"))
ns=int(input("enter no of symbols do you want in your password"))
for i in range(1,nc+1):
    ch=random.choice(letters)
    password_list.append(ch)
for i in range(1,np+1):
    ch=random.choice(numbers)
    password_list.append(ch)
for i in range(1,ns+1):
    ch=random.choice(symbols)
    password_list.append(ch)
random.shuffle(password_list)
password=""
for i in password_list:
    password+=str(i)
print(password)
