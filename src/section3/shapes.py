"""
Warm-up Question 2: Why Square/Rectangle breaks LSP
The calling code assumes that setting the height of a rectangle will leave its width completely unchanged. 
The square violates this assumption by linking the two dimensions together. 
This means we cannot substitute a square in place of a rectangle without breaking standard geometric expectations.
"""

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


def main():
    # Warm-up Question 1: Testing the classic Rectangle/Square issue
    rect = Square()
    rect.set_width(10)
    rect.set_height(20)
    
    # We expect 200, but this will print 400
    print(f"Area is: {rect.get_area()}")

if __name__ == "__main__":
    main()