#It is a little example of second-degree equation.
#In python we can make this equation


import logging

#first we define the variables
a= int(input("Enter 'a' number:"))
b= int(input("Enter 'b' number:"))
c= int(input("Enter 'c' number:"))

#2. I´ll divide the formula in diferents variables
squareRootSection =(b**2)-(4*a*c)
divider = 2*a

if squareRootSection > 0:
    squareRootSection = pow(squareRootSection,0.5) #or squareRootSection ** 0.5
    result1= (b*-1)+squareRootSection
    result2= (b*-1)-squareRootSection
    x1:float= (result1)/divider
    x2:float= (result2)/divider
    result = [result1, result2]
    print(result)
else:
    logging.warning('The square root section can not be calculated')