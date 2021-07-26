#Evaluate the below piecewise function using Python and print the value of y.
#y=x+2 (0<x<10)
#y=x^2+2 (10<=x)
#y=0 (otherwise)
#The value of the variable x should be an numerical input from the user.

x=int(input())
y1=x+2
y2=(x**2)+2
y3=(0)
if(0<x and x<10):
    print(y1)
if(10<=x):
    print(y2)
else:
    print(y3)