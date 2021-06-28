class Car:
    # set the numbers of Car object created
    # count is a class variable and to access it
    # within and outside the class use Car.count or
    # <Car instance name>.count
    count=0
    def __init__(self,name):
        self.name=name
        Car.count+=1
    def __del__(self):
        Car.count-=1
    
