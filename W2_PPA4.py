#Accept a string and return a new string formed using the middle three characters. If the input string is of even length, make the string of odd length as below
#Add a period . at the end if is not there
#Otherwise remove the period . from the end

s=str(input())
n=(len(s))
y=str('.')
if n%2==0:
    if s.isalnum():
        x=(s+y)
        k=(len(x)//2)
        print(s[k-1]+s[k]+s[k+1])
    else:
        z=s.strip('.')
        p=(len(z)//2)
        print(s[p-1]+s[p]+s[p+1])
else:
    q=(n//2)
    print(s[q-1]+s[q]+s[q+1])
