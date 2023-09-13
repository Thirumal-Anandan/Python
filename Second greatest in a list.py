#Program for finding the second greatest number in a list

l=[5, 7, 2, 9, 6]
m=max(l)
for i in range(len(l)):
    if (m==l[i]):
        print("Index of the greatest number is: ", i)
        break
del l[i]
print("The second greatest number of the list is: ", max(l))

'''
n=l.pop(i)
print(n)
'''

