class Car:
    # set the numbers of Car object created
    count=0
    def __init__(self,name):
        self.name=name
        Car.count+=1
    def __del__(self):
        Car.count-=1
    
