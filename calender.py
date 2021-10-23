d = input("Enter the first day of the month : ")

print("\n")
print("Mon\tTue\tWed\tThu\tFri\tSat\tSun")
d = (d.lower())[0:3]

if(d=="mon") : d = 1
if(d=="tue") : d = 2
if(d=="wed") : d = 3
if(d=="thu") : d = 4
if(d=="fri") : d = 5
if(d=="sat") : d = 6
if(d=="sun") : d = 7


for i in range ((d-1)) : print("  \t",end="")

for i in range (31) : 
    print(" ",end = "")
    print(i+1,end = "")
    if(d==7) : 
        print("\n",end="")
        d = 1
    else : 
        print("\t",end = "")
        d = d +1
    


