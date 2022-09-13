class NumbersArray:

    def __init__(self):
        self.__numbers=[]
    
    def getNumbers(self):
        return self.__numbers
    
    def setNumbers(self, rangeLimit:int=1):
        for i in range(rangeLimit):
            number = int(input("enter a number:"))
            self.__numbers.append(number)