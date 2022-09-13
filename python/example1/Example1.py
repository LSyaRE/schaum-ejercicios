class Example1:

    def __init__(self):
        self.__pi = 3.14159

    def area(self,rad: float) -> float:
        return self.__pi * (rad**2)


area:Example1 =Example1()


print("Area Calculator")
radius= float(input("Enter the radius of the circle:"))
area = area.rad(radius)
print(f"The Area is: {area}")