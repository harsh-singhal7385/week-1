def gcd(a, b):
    if (b == 0):
        return a
    if (a == 0):
        return b
 
    if (a == b):
        return b
 
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)


num1 = int(input("Enter first number : \n"))
num2 = int(input("Enter second number : \n "))
print(f"GCD of {num1} and {num2} is ::  ", gcd(num1, num2))