def emobstud(fname,lname,course):
    print(fname+lname+"Register a "+course)
emobstud("Drew ","Oliver","Javascript")
emobstud("Gina ","Oli","MIT")
emobstud("Vesyl ","Overa","Data science")
def rating():
    y=float(input("Rate me on a scale of 1-5 "))
    if y==5:
        print("Delighted")
    elif y==4:
        print("Alright")
    elif y==3:
        print("Inbetween")
    elif y==2:
        print("Why")
    elif y==1:
        print("Sorry")
    else:
        print("scale is 1-5")
rating()

def calcdivide():
    x=130
    y=int(input("Enter your Kenyan currency : "))
    print("Your money in $",y/x)
calcdivide()