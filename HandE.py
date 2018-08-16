import math
setA=list()
setB=list()
t=0
temp=0
mempos1=list()
mempos2=list()
number1=input("Enter No of elements in set A")
print("Enter membership values of setA")
for i in range(int(number1)):
    n1=input("Enter Member")
    n2=input("Enter Membership Value")
    mempos1.append(int(n1))
    setA.append(float(n2))
number2=input("Enter No of elements in set B")    
print("Enter membership values of setB")
for i in range(int(number2)):
    n1=input("Enter Member")
    n2=input("Enter Membership Value")
    mempos2.append(int(n1))
    setB.append(float(n2))
for i in range(int(number2)):
    count=0
    for x in range(int(number1)):
        if(mempos2[i]==mempos1[x]):
            t+=abs(setB[i]-setA[x])
            temp+=math.pow(setB[i]-setA[x],2)
            count+=1
    if(count==0):
        t+=abs(setB[i]-0)
        temp+=math.pow(setB[i]-0,2)        
print("Hamming Distance : ",t)
print("Eclidean Distance : ",math.sqrt(temp))    
            
    