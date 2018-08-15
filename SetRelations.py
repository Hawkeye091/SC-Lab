setA=list()
setB=list()
mempos1=list()
mempos2=list()
n1=int(input("Enter the number of elements in set A :\n"))
n2=int(input("Enter the number of elements in set B :\n"))
print("Enter elements of A\n")
for i in range(int(n1)):
    mempos1.append(int(input()))
    setA.append(float(input()))
print("Enter elements of B\n")    
for i in range(int(n2)):
    mempos2.append(int(input()))
    setB.append(float(input()))
print("Elements of Set A  : \n")    
for i in range(int(n1)):
    print(mempos1[i])
    print(setA[i])
print("Elements of Set B : \n")
for i in range(int(n2)):
    print(mempos2[i])
    print(setB[i])
R1=list()
R2=list()
for i in range(int(n1)):
    for k in range(int(n2)):
        R1.append(setA[i]+setB[k])
        R2.append(setA[i]-setB[k])
print("Relation R1 on Set A and B are : \n")        
for i in range(int(n1*n2)):
        print(R1[i])
print("Relation R2 on Set A and B are : \n")                
for i in range(int(n1*n2)):
        print(R2[i])        
ch=int(input("Enter Choice for Set Relations operations 1.Union 2.Intersection 3.Compliment\n"))       
if(ch==1):
   for i in range(n1*n2):
         print(max(R1[i],R2[i]))    
elif(ch==2):
   for i in range(n1*n2):
         print(min(R1[i],R2[i]))    
elif(ch==3):
    print("Compliment of R1 : \n")
    for i in range(n1):
         print(1-R1[i])    
    print("Compliment of R2 : \n")
    for i in range(n2):
         print(1-R2[i])    
    