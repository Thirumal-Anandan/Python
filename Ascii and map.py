'''
ls=[]
for i in range(65, 91):
    ch=chr(i)
    ls.append(ch)
print("List of variable names: ",ls)
n=int(input("Enter the number of inputs: "))
for j in range(n):
    print(ls[j])
    ls[j]=map(int, input("Enter a number: ").split())
'''
ls = []
for i in range(65, 91):
    ch = chr(i)
    ls.append(ch)
print("List of variable names: ", ls)
print()
n = int(input("Enter the number of inputs: "))
inputs = {}
for j in range(n):
    var_name = ls[j]
    print(var_name)
    user_input = input("Enter a number: ")
    inputs[var_name] = int(user_input)
print("Individual variables:")
for var_name, value in inputs.items():
    print(var_name ,'=',value)
