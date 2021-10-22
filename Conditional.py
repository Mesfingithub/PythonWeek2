#>90, "A", >80, "B" >70, "C", >60, "D", <=50, "F"
mark= int(input("Please inter Gread"))
if mark>90:
    Gread="A" 
elif mark>80:
    Gread="B"
elif mark>70:
    Gread="C"
elif mark>60:
    Gread="D"
else:
    Gread="F"
print (Gread)