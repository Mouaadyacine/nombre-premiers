n=int(input("enter a integer"))
ca=0
b=""
for i in range(2,n):
    for j in range(1,-1):
     if i%j==0:
        ca==ca+1
        if ca==2:
           b==b+i
print(b)

  