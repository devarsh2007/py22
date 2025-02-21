# hirarichal inheritance

class vehicals:
    def start(self):
        print("start vehical")
        
    def stop(self):
        print("stop vehical")
        
class car(vehicals):
    def fast(self):
        print("car is fast")
        
class bus(vehicals):
    def multiple_seat(self):
        print("bus has multiple seats")
        
        
c1 = car()
c1.start()
c1.stop()
c1.fast()
    
b1 = bus()
b1.start()
b1.stop()
b1.multiple_seat()