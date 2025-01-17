import copy

def ex():
    a = [1,[2,3],3]

    return(a)
'''
To understand how reference works in python.
Use the comments to see how different assignments result in differnt copies
'''

def abc(x):
   change = x                               #Simple reference
#    change = x[:]                          #Shallow copy
#    change = list(x)                       #Shallow copy
#    change = copy.deepcopy(x)              #Deep copy
    change[1].append(4)
    change[0] = 10

    return change

intial = ex()
middle = abc(intial)

print(intial)
print(middle)
