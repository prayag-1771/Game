import random
import time
def now(x):
    global m
    m=random.randrange(x)
    print(m)
    print(" "*m+"__")
leng=eval(input("ENTER THE GAME AREA SIZE:"))
now(leng)
count=0
while 1:
    def spacecraft(y):
        print(" "*y+"    *****\n"+" "*y+"  *********\n"+" "*y+"*************\n"+" "*y+"    ****")
        global count
        count+=2
    b=0
    def scposition(a,z=0):
        if a=="d":
            z+=1
            return z
        elif a=="a":
            z-=4
            return z
    def fire(g,count):
        if g=="w":
            for p in range(11):
                time.sleep(0.5)
                global m
                print(m)
                print(" "*m+"__"+"\n"*(11-p),end="")
                print(" "*(count+6)+"^"+"\n"*p)
                spacecraft(count)
                print(count+8,m)

            if (count+8)==(m+3):
                print("You win")
            elif (count+8)==(m+2):
                print("You win")
            else:
                print("You didnt")
        else:
            print()

    b=input()
    c=scposition(b)
    count+=c
    spacecraft(count)
    g=input()
    fire(g,count)
    