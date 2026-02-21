r='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

p='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

s='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

print("Welcome to rock paper scissor game")

import random

n=int(input("Enter 0 for rock,1 for paper and 2 for scissors"))
print("Your input:")
if n==0:
    print(r)
elif n==1:
    print(p)
else:
    print(s)

k=random.randint(0,2)
print("Computer Input:")
if k==0:
    print(r)
elif k==1:
    print(p)
else:
    print(s)

print()

if k==n:
    print("Its draw")
elif (n==0 and k==1) or (n==1 and k==2) or (n==2 and k==0):
    print("Computer wins")
else:
    print("You win")
    





















