def getSumSquare(x,y):
    ans = (x+y)**2
    return ans

num1 = int(input("Enter first number : \n"))
num2 = int(input("Enter second number : \n"))

result = getSumSquare(num1,num2)
print("Result : \n", result)