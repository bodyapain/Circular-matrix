a=int(input())
n=1
matrix=[[0 for i in range(a)] for i in range(a)]
j=0
i=0
m=1
k=0
while True:
    while j!=a-m:
        matrix[i][j]=n
        if n == a**2:
            break
        j=j+1           
        n+=1
    if n == a**2:
        matrix[i][j]=n
        break
    while i!=a-m:           
        matrix[i][j]=n 
        if n == a**2:
            break   
        i=i+1     
        n+=1
    if n == a**2:
        matrix[i][j]=n
        break
    while j!=k:    
        matrix[i][j]=n
        if n == a**2:
            break 
        j=j-1   
        n+=1
    if n == a**2:
        matrix[i][j]=n
        break
    while i!=m:    
        matrix[i][j]=n
        if n == a**2:
            break
        i=i-1
        n+=1 
    if n == a**2:
        matrix[i][j]=n
        break   
    k+=1
    m+=1
    
for i in range(a):
    for j in range(a):
        print(matrix[i][j],end=' ')
    print()    