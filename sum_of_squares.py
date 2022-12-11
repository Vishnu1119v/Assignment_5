class Point:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self):
        sum=self.x**2+self.y**2+self.z**2
        return f'The sum of squares of given numbers is: {sum}'
obj1=Point(1,3,5)
print(obj1.sqSum())