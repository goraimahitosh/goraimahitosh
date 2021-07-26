#Evaluate the output d based on three given Boolean inputs a, b and c.
#d=f(a,b,c)
#     a       b       c       d
#   False   False   False   False
#   False   False   True    True
#   False   True    False   False
#   False   True    True    True
#   True   False    False   True
#   True   False    True    True
#   True   True     False   False
#   True   True     True    True

print('d=(a,b,c)')
print('Enter the values of a, b and c (True or False)')
print('Enter a (True or False)')
a=input()
print('Enter b (True or False)')
b=input()
print('Enter c (True or False)')
c=input()
if (a=='False'):
    if (c=='False'):
        print ('Value of d=')
        print ('False')
    else:
        print ('Value of d=')
        print ('True')
if (a=='True'):
    if (c=='True' and b!='True'):
        print ('Value of d=')
        print ('True')
    elif (b=='True' and c=='True'):
        print ('Value of d=')
        print ('True')
    elif (b=='False' and c=='False'):
        print ('Value of d=')
        print ('True')
    else: 
        print ('Value of d=')
        print ('False')
