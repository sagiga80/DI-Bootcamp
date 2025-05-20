# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None and diameter is not None:
            if radius == diameter/2:
                print("valid input")
            else:
                raise ValueError("invalid input: incorrect ratio between radius and diameter")
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Must provide either radius or diameter.")

# Other abilities of a Circle instance:
# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
    @property
    def area(self):
        return 3.14 * self.radius ** 2
    def __str__(self):
        return f"Circle with radius: {self.radius:.2f}, area: {self.area:.2f}"
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("the second object is not a Circle!")

# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        raise TypeError("the second object is not a Circle!")
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        raise TypeError("the second object is not a Circle!")
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        raise TypeError("the second object is not a Circle!")

# Examples:
c1 = Circle(radius=3)
c2 = Circle(diameter=8)
c3 = Circle(radius=5)

print(c1)            # Circle with radius: 3.00, diameter: 6.00, area: 28.27
print(c2.area)       # Area value
print(c1 + c2)       # New Circle object
print(c3)
print(c1 == c2)      # False
print(c1 < c2)       # True
print(c3 > c1)
print(c2 > c3)

# Put in a list and sort
circles = [c3, c1, c2]
for circle in circles:
    print(circle)
sorted_circles = sorted(circles)
for circle in sorted_circles:
    print(circle)       # Sorted by radius
