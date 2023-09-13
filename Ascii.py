ls=[]
for i in range(65, 91):
    ch=chr(i)
    ls.append(ch)
print("List of variable names: ",ls)
n=int(input("Enter the number of inputs: "))
for j in range(n):
    print(ls[j])
    ls[j]=map(int, input("Enter a number: ").split())

    
    
