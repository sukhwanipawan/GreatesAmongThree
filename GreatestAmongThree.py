"""Write a code to take three values from user and find the greatest number from them"""

x = float(input("Enter the 1st number"))
y = float(input("Enter the 2nd number"))
z = float(input("Enter the 3rd number"))
if x<y :
    if z<y :
        print('The greatest number is', y)
    else :
        print('The greatest number is', z)
elif y<x :
    if z<x :
        print('The greatest number is', x)
    else :
        print('The greatest number is', z)
print('byeee')