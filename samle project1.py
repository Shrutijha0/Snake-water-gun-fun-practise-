import random
def gamewin (comp, you):


    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    elif comp==you:
        return None
        

print("comp turn : snake , water or gun?")
randno=random.randint(1,3)
if randno == 1:
    comp="s"
elif randno==2:
    comp="w"
elif randno==3:
    comp="g"

you=input("your trun: snake water or gun?")
a = gamewin(comp,you)

print(f"comp choose{comp}")
print(f"you choose{you}")

if a == None:
    print("its a tie")
elif a==True:
    print("you win")
else:
     print("you loose")

     

    
