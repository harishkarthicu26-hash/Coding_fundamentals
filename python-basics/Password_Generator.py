print("Welcome to the password generator!")
import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'
symbols = '!#$%&()*+'
l=int(input("How much letters do you want in your password"))
n=int(input("How much numbers do you want in your password"))
s=int(input("How much symbols do you want in your password"))

password=" "
for i in range(1,l+1):
    ran=random.choice(letters)    
    password=password+ran
for i in range(1,n+1):
    ran=random.choice(numbers)
    password=password+ran
for i in range(1,s+1):
    ran=random.choice(symbols)
    password=password+ran
k=list(password)
random.shuffle(k)
final_password=""
for char in k:  
    final_password=final_password+char      
print(f"Your password is {final_password}")
