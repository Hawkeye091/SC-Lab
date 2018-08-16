import math
setA=list()
setB=list()
t=0
temp=0
number=input("Enter No of elements in both sets")
print("Enter membership values of setA")
for i in range(int(number)):
    n=input("Enter Membership value")
    setA.append(float(n))
print("Enter membership values of setB")
for i in range(int(number)):
    n=input("Enter Membership value")
    setB.append(float(n))
for i in range(len(setA)):
    t+=abs(setB[i]-setA[i])
    temp+=math.pow(setB[i]-setA[i],2)
print("Hamming Distance : ",t)
print("Eclidean Distance : ",math.sqrt(temp))    
            
    