import logging
import math


class Example7:
    def __init__(self):
        self.pi= 3.14159

    def getArea(self,radius):
        return self.pi * (radius**2)
    
    def getRadius(self,area):
        if area < 0:
            logging.warning("Area is negative")
            return area
        return (area/self.pi)**0.5

    def proabilityW(self,u,v):
        return (u-v)/(u+v)
    
    def elementalFormula(self,x):
        return 100*(1+x+(2*(x**2))+(3*(x**3)))
    
    def hypotennuse(self,base,height):
        return ((base**2)+(height**2))**0.5

example7 = Example7()


result1 = example7.elementalFormula(1)
print(result1)
result2 = example7.proabilityW(3,2)
print(result2)
result3 = example7.hypotennuse(8,6)
print(result3)
