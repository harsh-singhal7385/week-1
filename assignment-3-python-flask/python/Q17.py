
from decimal import DivisionByZero  
def divideByZero():  ########### DivisionByZero
    try:
        print(5/0)
    except DivisionByZero as error:
        print(error)





def typeError():  ########### TypeError
    try:
        a=1.4
        b='0'
        print(a+b)
    except TypeError as error:
        print("Type Error, cannot integer with string")





def valueError():  ###########  ValueError
    a = "hi"
    try:
        a = int(input('Enter a number: '))
        ## press ctrl+c from  keyboard to get it
    except ValueError:
        print("ValueError : That was no valid number.")





def indexError():  ###########  IndexError
    try:
        arr = [1,2,3,4,5]
        print( arr[10] )
    except IndexError as error:
        print("IndexError : list index out of range")





def nameError():  ###########  NameError
    try:
        s = "hello world"
        print(ss)
    except NameError as error:
        print("NameError : name ss is not defined")


### by commenting others functions at a time else again error :)

divideByZero()
typeError()
valueError()
indexError()
nameError()