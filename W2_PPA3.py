#Write a Python code to realize the equation of a line given 2 points (x1,y1) and (x2,y2). The input is in 5 lines where , the first, second, third, and fourth line rperesent x1,y1,x2 and y2 respectively. The fifth line corresponds to x3. Determine y3 using line equation given below.
#(x-x1)/(x2-x1)=(y-y1)/(y2-y1)
#the output should be vertical Line if line is vertical. In order cases, the output should be 2 lined, where the first line is the value of y3 and the second line indicates whether the slope of the line is positive or negative. Print positive slope, Negative Slope and Horizontal Line accordingly.

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3= float(input())
if x1!=x2:
    #if x1 and x2 become similar then x2-x1 become zero
    #(x3-x1)/(x2-x1)=(y3-y1)/(y2-y1)
    #1/m=(x3-x1)/(y3-y1)=(x2-x1)/(y2-y1)
    m=(y2-y1)/(x2-x1)
    y3=y1+m*(x3-x1)
    print(y3)
    if m==0:
        print('Horizontal Line')
    elif m>0:
        print('Positive Slope')
    else:
        print('Negative Slope')
else:
    print('Vertical Line')