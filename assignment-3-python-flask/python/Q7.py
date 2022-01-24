input_str = input("Enter the string \n: ")
if  len(input_str) > 0:
    if input_str[:2] == 'Is':
        print("Result : ", input_str)
    else:
        output_str = "Is"+input_str
        print("Result : ", output_str )
else:
    print("Is")