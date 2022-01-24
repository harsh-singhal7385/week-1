
import re
str = "June 03 2007"   # Given input
l = str.split(" ")

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

if l[0].lower() in months and re.findall("[0-3][0-9]", l[1]) and len(re.findall("\d", l[2])) == 4:
    
    if (months.index(l[0].lower())+1) == 2 :
        if int(l[2]) % 400 == 0 and int(l[1]) <= 29:
            print("Date is Valid date / proper date")
        elif int(l[2]) % 400 != 0 and int(l[1]) <= 28:
            print("Date is Valid date / proper date")
        else:
            print("Date is not Valid date / improper date")
            
    elif (months.index(l[0].lower())+1) % 2 == 0 and (months.index(l[0].lower())+1) != 2:
        if int(l[1]) <=30:
            print("Date is Valid date / proper date")
        else:
            print("Date is not Valid date / improper date")

    elif int(l[1]) <=31 and (months.index(l[0].lower())+1) != 2:
        print("Date is Valid date / proper date")
        
    else:
        print("Date is not Valid date / improper date")
    
else:
    print("Date is not Valid date / improper date")
