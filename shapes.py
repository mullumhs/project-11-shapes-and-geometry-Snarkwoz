class Shapes():
    def __init__(self,shape_type):
        self.type = shape_type

class Rectangle(Shapes):
    def __init__(self,shape_type,height,length):
        super().__init__(self,shape_type)
        self.type = shape_type
        self.height = height
        self.length = length

    def calc_area(self):
        print(f"The area of your ractangle is {self.height * self.length}.")


rect1 = Rectangle("square","5","2")
rect1.calc_area()