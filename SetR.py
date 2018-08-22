setA=list()
setB=list()
setC=list()
temp1=list()
temp2=list()
temp3=list()
n1=int(input("Enter the number of elements in set A :\n"))
n2=int(input("Enter the number of elements in set B :\n"))
n3=int(input("Enter the number of elements in set C :\n"))
print("Enter elements of A\n")
for i in range(int(n1)):
    setA.append(float(input()))
print("Enter elements of B\n")    
for i in range(int(n2)):
    setB.append(float(input()))
print("Enter elements of C\n")    
for i in range(int(n3)):
    setC.append(float(input()))    
print("Elements of Set A  : \n")    
for i in range(int(n1)):
    print(setA[i])
print("Elements of Set B : \n")
for i in range(int(n2)):
    print(setB[i])
print("Elements of Set C  : \n")    
for i in range(int(n3)):
    print(setC[i])    
R1=list()
R2=list()
R3=list()
R4=list()
R5=list()
for i in range(int(n1)):
    for k in range(int(n2)):
        R1.append(setA[i]+setB[k])
        R2.append(setA[i]-setB[k])
for i in range(int(n2)):
    for k in range(int(n3)):
        R3.append(setB[i]*setC[k])
print("Relation R1 on Set A and B are : \n")        
for i in range(int(n1*n2)):
        print(R1[i])
print("Relation R2 on Set A and B are : \n")                
for i in range(int(n1*n2)):
        print(R2[i])        
print("Relation R3 on Set A and B are : \n")                
for i in range(int(n2*n3)):
        print(R3[i])               
ch=1
count=0
while(ch):
  ch=int(input("Enter Choice for Set Relations operations 1.Union 2.Intersection 3.Compliment 4.Containment 5.Max Min Product 6.Max Product\n"))                 
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
  elif(ch==4):
     print("Containment of Set A in Set B") 
     for i in range(n1*n2):
        if(R1[i]>R2[i] or R1[i]==R2[i]):
           print(R2[i])
           count+=1
     if(count==0):
         print("No Values Contained")            
  elif(ch==5):
     m=0
     while(m<(n2*n2)):
         n=0
         while(n<n3):  
             temp1=min(R1[m],R3[n])
             temp2=min(R1[m+1],R3[n+n3])
             temp3=max(temp1,temp2)
             R4.append(temp3)
             n+=1    
         m+=n2  
     for i in range(n1*n3):
         print(R4[i])    
  elif(ch==6):
     m=0
     while(m<(n2*n2)):
         n=0
         while(n<n3):  
             temp1=R1[m]*R3[n]
             temp2=R1[m+1]*R3[n+n3]
             temp3=max(temp1,temp2)
             R5.append(temp3)
             n+=1    
         m+=n2  
     for i in range(n1*n3):
         print(R5[i])    