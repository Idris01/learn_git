class Car:
    def __init__(self,maker,wheel=4):
        self.maker=maker
        self.wheel=wheel

    @property
    def maker(self):
        return self.maker

    def __str__(self):
        return "%s with %s" % (self.maker,self.wheel)
