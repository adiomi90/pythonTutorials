from abc import ABC, abstractmethod

class UIControl(ABC):
    
    @abstractmethod   
    def draw(self):
        pass

    
class TestBox(UIControl):
    @abstractmethod
    def draw(self):
        print("drawing a testbox")
    

class DropDownList(UIControl):
    def draw(self):
        print("drawing a dropdown")
        

def draw(controls):
    for control in controls:
        control.draw()
    
    
ddl = DropDownList()


testbox = TestBox()
draw([ddl, testbox])



