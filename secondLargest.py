#prints the second largest number out of three numbers

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

if( (a > b and b > c) or (c > b and b > a)):
    print(f"{b} is second largest")
elif( (b > a and a > c) or (c > a and a > b)):
    print(f"{a} is second largest")
else:
    print(f"{c} is second largest")
    
