def num_square(num):
    print(input_num)
    square= num * num

    return square


input_num = 101

if input_num > 100:
    result = num_square(5)


print(result)


'''
Q1. What is the scope of num,square, input_num, result?
Ans-1 : num -> num is a local variable.  It can only used inside the function.
square -> square is also a local variable.  It can only used inside the function.
input_num -> input_num is a global variable. It can be used inside or outside ( anywhere )  the function.
result -> num is also a local variable. It can only used inside the if condition.


Q2. What is the lifetime of each variable? When will they be created and destroyed?
Ans-2 : 1->Local variables including function parameters have a life from the start of the execution of 
the function to the end of execution - i.e. the end of the function or the return statement.

2 -> Global variables life from when the module is imported until 
the end of the application - unless the variable is explicitly deleted.


Q3. What would happen if input_num had a value of less than 100?
Ans-3 : If input_num is less than 100 then it will throw an error that 
'result variable is not defined'. now if we declare result variable out of function to any value ,
then the program will be execute and print that value.


Q4. What would be the scope and value of `result` if input_num has a value of less than 100?
Ans-4 : Firstly 'result' is a local variable. The scope of result is valid only inside function. 
And if the input_num value is less than 100 then it'll throw an error that 'result' variable is not defined.
'''