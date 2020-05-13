import numpy as np
import graph


class Matrix:

    def __init__(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def add(self, x, y):
        self.__init__(x, y, z)
        result = np.add(self.x, self.y)
        return result

    def sub(self, x, y):
        self.__init__(x, y, z)
        result = np.subtract(self.x, self.y)
        return result

    def mult(self, x, y):
        self.__init__(x, y)
        result = np.multiply(self.x, self.y)
        return result

    def det(self, x):
        self.__init__(x)
        result = np.linalg.det(self.x)
        return "%.2f" % round(result, 2)
        
    def trans(self,x):
        self.__init__(x)
        result=np.transpose(x)
        return result

    def inv(self,x):
        self.__init__(x)
        result=np.linalg.inv(x)
        return result 

matrix = Matrix()
# x1 = [[1, 2], [3, 0]]
# x2 = [[1, 3], [2, 3]]
# x3 = matrix.add(x1, x2)
# print(x3)
