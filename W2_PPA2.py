#Write a Python code to find the quadrant of a point taken as input from the user. The input is given in 2 lines with the first and second lines representing the x coordinate and y coordinate of the point respectively. The possible outputs are I, II, III, IV, X-axis, Y-axis and Origin. Any other output will not be accepted, Take care of the upper and lower cases while printing the output.

x=float(input())
y=float(input())
if(x==0 and y==0):
    print("Origin")
elif(x==0 and y>0):
    print("Y-axis")
elif(x==0 and y<0):
    print("Y-axis") 
elif(y==0 and x>0):
    print("X-axis")
elif(y==0 and x<0):
    print("X-axis")
elif(x>0 and y>0):
    print("I")
elif(x>0 and y<0):
    print("IV")
elif(x<0 and y>0):
    print("II")
elif(x<0 and y<0):
    print("III")