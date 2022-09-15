import logging

#Determine the area and radius
class Example6:
    def __init__(self):
        self.pi= 3.14159

    def getArea(self,radius):
        return self.pi * (radius**2)
    
    def getRadius(self,area):
        if area < 0:
            logging.warning("Area is negative")
            return area
        return (area/self.pi)**0.5

circle = Example6()
