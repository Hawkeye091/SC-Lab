
setA = {}


print("Enter the number of elements in set A")
sizeA=int(input())

print("Enter the elements of A and their membership values")
for i in range(sizeA):
    qw = input().split()
    b = int(qw[0])
    c = float(qw[1])
    setA[b] = c

setB={}

print("Enter the number of elements in set B")
sizeB=int(input())

print("Enter the elements of B and their membership values")
for i in range(sizeB):
    qw = input().split()
    b = int(qw[0])
    c = float(qw[1])
    setB[b] = c

uni={}
for i in setA.keys():
    if i in setB:
        uni[i]=max(setA[i],setB[i])
    else:
        uni[i]=setA[i]

for j in setB.keys():
    if not j in setA:
        uni[j]=setB[j]

inter={}
for i in setA.keys():
    if i in setB:
        inter[i]=min(setA[i],setB[i])

compA={}
for i in setA.keys():
    compA[i]=1-setA[i]

compB={}
for i in setB.keys():
    compB[i]=1-setB[i]  

dif={}
for i in setA.keys():
    if not i in setB:
        dif[i]=setA[i]

for i in range(40):
    print("-",end='')
print("")
    
print("SetA")
print(setA)

for i in range(40):
    print("-",end='')
print("")
    
print("SetB")
print(setB)    

for i in range(40):
    print("-",end='')
print("")
print("Union")
print(uni)

for i in range(40):
    print("-",end='')
print("")    
print("Intersection")
print(inter)

for i in range(40):
    print("-",end='')
print("")    
print("Difference")
print(dif)

for i in range(40):
    print("-",end='')
print("")    

print("Complement of A")
print(compA)


for i in range(40):
    print("-",end='')
print("")
    
print("Complement of B")
print(compB)

for i in range(40):
    print("-",end='')
print("")    
    
    