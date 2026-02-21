list=["apple","banana","cherry"]

import random

word=random.choice(list)

a=(len(word)*"_ ")

print(a)
game_over=False
lives=6
l=[]
while not game_over:
    
    n=input("Enter a letter to guess:\n").lower()
    d=""
    
    for i in word:
        if i == n:
            d=d+n
            l.append(n)
        elif i in l:
            d=d+i
        else:
            d=d+"_ "
    print(d)

    if n not in word:
        lives=lives-1
        if lives==0:
            game_over= True
            print("You Lose")
        

    if "_" not in d:
        game_over=True
        print("You Win")
