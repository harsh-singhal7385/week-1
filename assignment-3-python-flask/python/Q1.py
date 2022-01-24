data = input()

length = len(data)

if length <= 1:
    print("Empty String")
    
elif length == 2:
    data = data*2
    print(data)
    
else:
    start = data[:2]  
    end = data[-2:]
    output = start + end
    print(output)