output = []

class MyErrorClass(Exception):
 
    def __init__(self, age, name, email, phone_num):
        self.age = age
        self.name = name
        self.email = email
        self.phn = phone_num

    
    def checkName(self):           
        try:
            if len(self.name) >= 3:
               output.append(self.name)
            else:
                raise MyErrorClass("","Exception InvalidNameError: Name length must be greater than 3","","")
        except MyErrorClass as error:
            print(error.name)
    
    def checkAges(self):  
        try:
            if self.age > 0:
                output.append(self.age)
            else:
                raise MyErrorClass("Exception AgeInvalidError: Age must be greater than 0","","","")
        except MyErrorClass as error:
            print(error.age)
            
            
    def checkEmail(self):   
        try:
            if '.' in self.email and '@' in self.email:
               output.append(self.email)
            else:
                raise MyErrorClass("","","Exception InvalidEmailError: Email must contains @ and .","")
        except MyErrorClass as error:
            print(error.email)
            
    def checkPhoneNum(self):   
        try:
            if len(self.phone_num) == 10:
                output.append(self.phone_num)
            else:
                raise MyErrorClass("","","","Exception InvalidPhoneNumError: Phone number should be 10 digits")
        except MyErrorClass as error:
            print(error.phone_num)
        

obj = MyErrorClass(21, "abc", "abc@quantiphi.com", "9988776655")  
obj.checkAges()
obj.checkName()
obj.checkEmail()
obj.checkPhoneNum()
if len(output) == 4:
    print("All values are valid")
else:
    print("Some values are invalid")