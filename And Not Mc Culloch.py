Tabl=[[0,0,0],
      [0,1,0],
      [1,0,1],
      [1,1,0]]

x1=int(input("Enter Input 1"))
x2=int(input("Enter Input 2"))

w1=int(input("Enter Weight 1"))
w2=int(input("Enter Weight 2"))

if(w1>0 and w2 >0):
    theta=[1*w1,2*w2]
elif ((w1 >0 and w2<0) or (w1 <0 and w2>0)):
    if(w1>0):
        theta=[1*w1-1,3]
    else:
        theta=[1*w2-1,3]
        
y1=(x1*w1+(1-x2)*w2)

for i in range(theta[0],theta[1]):
    print("For thereshold "+i)
    if(y1>=i):
        print(1)
    else:
        print(0)    
