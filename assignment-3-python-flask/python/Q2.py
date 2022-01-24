li = []
print("Enter the nos of elements")
n = int(input())

print("Enter the elements in straight line separated by space")

li = list(map(int,input().split()))

max = 0

print("Maximum number is : ")

if len(li) == 1:
    max = li[0]
    print(max)
else:
    for i in li:
        if max<i:
            max = i

    print(max) 