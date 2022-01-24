class Shapes:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def shape_1(self):
        print(f"Shape: shape_1 call and Variable 1 = {self.var1}")
        
    def shape_2(self):
        print(f"Shape: shape_2 call and Variable 2 = {self.var2}")
    

class Triangle(Shapes):
    def __init__(self, var3,var1, var2):
        self.var3 = var3
        Shapes.__init__(self,var1,var2)
    
    def shape_1(self):
        print(f"Shape: Overidden shape_1 method call in Triangle and Variable 1 = {self.var1}")
    
    def triangle_1(self):
        print(f"Triangle: triangle_1 call and Variable 1 = {self.var3}")

class ChildTriangle(Triangle):
    def __init__(self, var4, var3, var1, var2):
        self.var4 = var4
        Triangle.__init__(self,var3,var1,var2)
        
    def triangle_1(self):
        print(f"Triangle: Overridden triangle_1 call in ChildTriangle and Variable 1 = {self.var3}")
    
    def child_1(self):
        print(f"ChildTriangle: child_1 method call and Variable 1 = {self.var4}")
        

class Quadrilateral(Shapes):
    def __init__(self, var5, var1, var2):
        self.var5 = var5
        Shapes.__init__(self,var1,var2)
    
    def shape_2(self):
        print(f"Shape: Overidden shape_2 method call in Quadrilateral and Variable 1 = {self.var2}")

    
    def quadrilateral_1(self):
        print(f"Quadrilateral: quadrilateral_1 call and Variable 1 = {self.var5}")


class ChildQuadrilateral(Quadrilateral):
    def __init__(self, var6, var5, var1, var2):
        self.var6 = var6
        Quadrilateral.__init__(self,var5,var1,var2)
        
    def quadrilateral_1(self):
        print(f"Quadrilateral: Overridden quadrilateral_1 call in QuadrilateralChild and Variable 1 = {self.var5}")
    
    def child_quadrilateral_1(self):
        print(f"ChildQuadrilateral: child_quadrilateral_1 method call and Variable 1 = {self.var6}")
        

shape_1 = 40
shape_2 = 44
triangle_1 = 67
child_triangle_1 = 101
quadrilateral_1 = 78
child_quadrilateral_1 = 105

 
shapes = Shapes(shape_1, shape_2)                            


triangle = Triangle(triangle_1, shape_1, shape_2)                         
child_triangle = ChildTriangle(child_triangle_1, triangle_1, shape_1, shape_2)


quadrilateral = Quadrilateral(quadrilateral_1, shape_1, shape_2)                        
child_quadrilateral = ChildQuadrilateral(child_quadrilateral_1,quadrilateral_1, shape_1, shape_2)




shapes.shape_1()                         
shapes.shape_2()
print("*"*90)


triangle.shape_1()                      
triangle.triangle_1()
print("*"*90)

child_triangle.triangle_1()                
child_triangle.child_1()
print("*"*90)


quadrilateral.shape_2()                     
quadrilateral.quadrilateral_1()
print("*"*90)

                         
child_quadrilateral.quadrilateral_1()                 
child_quadrilateral.child_quadrilateral_1()
