class Country:
    def __init__(self, country_name, country_code):
        self.avg_population = 500000
        self.country_name = country_name
        self.country_code = country_code
        
        try:
            if not ( country_name.isdigit()) and not (country_code.isdigit()) and (len(country_code)==3): 
                print(country_name, country_code)
            else:
                raise ValueError("ValueError: Exception has occured either country name or code is incorrect")
        except ValueError as error:
            print(error)
            
    def country_short_form(self):
        print(self.country_name[:2].upper())
    
    def is_densly_populated(self, population):
        if population > self.avg_population:
            print(f"Population is greater than avg population = {True}")
        else:
            print(f"Population is greater than avg population = {False}")
           
    @staticmethod
    def world_avg_population(arr):
        print(f"Average Population = {sum(arr) / len(arr)}")

    @property
    def formatted_country_name(self):
        print(self.country_name + "( " + self.country_code + " )")              
           
     
    @formatted_country_name.setter
    def formatted_country_name(self, country_n, country_c):                    
        self.country_name = country_n
        self.country_code = country_c
  
 
    @formatted_country_name.deleter
    def formatted_country_name(self):                                                        
        self.country_name = ""
        self.country_code = ""
        
        

obj = Country("India", "IND")           


obj.country_short_form()                 

obj.is_densly_populated(500300)        


arr = [300000, 1500000, 2000000, 1300000, 900000]     
obj.world_avg_population(arr)


obj.formatted_country_name                


obj.country_name = "Africa"               
obj.country_code = "AFR"
obj.formatted_country_name


del obj.formatted_country_name
obj.formatted_country_name
