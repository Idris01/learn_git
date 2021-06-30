class Shape:
    """
    Represents any kind of shape
    """
    # the number of shape instance created
    count=0

    def area(self):
        pass

    def perimeter(self):
        pass

    class Meta:
        abstract=True


class Circle(Shape):
    pass
