
setA=list()
setB=list()
t1=0
t2=0
R1=list()
R2=list()
mempos1=list()
mempos2=list()
number=input("Enter No of elements in set A and B")
print("Enter membership values of setA")
for i in range(int(number)):
    n1=input("Enter Member")
    n2=input("Enter Membership Value")
    mempos1.append(int(n1))
    setA.append(float(n2))    
print("Enter membership values of setB")
for i in range(int(number)):
    n1=input("Enter Member")
    n2=input("Enter Membership Value")
    mempos2.append(int(n1))
    setB.append(float(n2))
for i in range(int(number)):
    for x in range(int(number)):
            t1=setB[i]+setA[x]
            R1.append(t1)
for i in range(int(number)):
    for x in range(int(number)):
            t1=setB[i]*setA[x]
            R2.append(t1)            
n=int(input("Enter Choice 1.Union 2.Intersection 3.Compliment"))          
U=list()
I=list()
C1=list()
C2=list()
if(n==1):
    for i in range(len(R1)):
            U.append(max(R1[i],R2[i]))
    for i in range(len(U)):        
            
if(n==2):
    for i in range(len(R1)):
            I.append(min(R1[i],R2[i]))
if(n==3):
    for i in range(len(R1)):
            C1.append(1-R1[i])
            C2.append(1-R1[i])            
   
    
            
    