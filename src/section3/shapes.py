"""
Warm-up Question 2: Why Square/Rectangle breaks LSP
The caller code expects that altering the height of a rectangle will never impact its width. A square breaks this geometric contract by locking both dimensions together, making it impossible to seamlessly substitute a rectangle with a square without causing unexpected behavior.
"""
class Rectangle:
    def __init__(self):
        self.w = 0
        self.h = 0

    def set_w(self, val):
        self.w = val

    def set_h(self, val):
        self.h = val

    def calc_area(self):
        return self.w * self.h

class Square(Rectangle):
    def set_w(self, val):
        self.w = val
        self.h = val

    def set_h(self, val):
        self.w = val
        self.h = val

def main():
    shape = Square()
    shape.set_w(10)
    shape.set_h(20)
    
    print(f"Calculated Area: {shape.calc_area()} (Expected 200)")

if __name__ == "__main__":
    main()