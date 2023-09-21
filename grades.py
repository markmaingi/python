grd=int(input("Enter grade:"))

if grd<=100 and grd>=80:
    print("A")
elif grd<=79 and grd>=60:
    print("B")
elif grd<=59 and grd>=50:
    print("C")
elif grd<=49 and grd>=30:
    print("D")
elif grd<=30 and grd>=0:
    print("Fail")

else:
    print("invalid input")