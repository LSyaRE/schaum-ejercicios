class Example8:
    def __init__(self,L,W):
        self.L = L
        self.W = W

    def getArea(self):
        return self.L *self.W
    
    def getPerimeter(self):
        return 2*(self.L + self.W)