class Car:
   
    # set the numbers of Car object created
    # count is a class variable and to access it
    # within and outside the class use Car.count or
    # <Car instance name>.count

    count=0

    def __init__(self,maker,name,wheel=4):
        self.maker=maker
        self.wheel=wheel
        self.name=name
        Car.count+=1

    def __del__(self):
        Car.count-=1
    
    def __str__(self):
        return "%s from %s" % (self.name,self.maker)
   
    @property
    def maker(self):
        return self.maker
 
