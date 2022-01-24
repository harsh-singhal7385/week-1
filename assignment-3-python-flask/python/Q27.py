flag = True
while(flag):
    ans = input("Do you want to update (y,n) : ")

    if ans.lower() == 'y':
        with open('sample.csv','r+') as f:
            f.seek(len(f.read())+5)
            line = input("Enter data or line : ")
            f.write("\n")
            f.write(line)
            print("My Data has been Appended Successfully to file named sample.csv file")
            f.close()
        
        with open('sample.csv','r') as f1:    
            for i in f1.readlines():
                print(i,end='')
    
    else:
        flag = False