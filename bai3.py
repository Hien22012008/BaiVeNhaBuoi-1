class Rectangle:
    def __init__(self, width, height):
        self.width = width 
        self.height = height

    def perimeter(self):
        return 2* (self.width + self.height)
    
    def area(self):
        return self.width * self.height
    
class Squared(Rectangle):
    def __init__(self, slide_length):
        super().__init__(slide_length, slide_length)

#Các canh của hình vuông và hình chữ nhật 
a = float(input("Input number: "))
b = float(input("Input number: "))
c = float(input("Input number: "))

squared = Squared(a)
rectangle = Rectangle(b, c)

# Tính chu vi và diện tích 
print(f"Squared perimeter: {squared.perimeter()}")
print(f"Squared area: {squared.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Rectangle area: {rectangle.area()}")