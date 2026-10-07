from utils.IO import IO

#single input instead of multiple
class qIO(IO):
    def __init__(self):
        super().__init__(0, 1)
    
    def ask_input(self):
        raw_input = str(input("Enter An Option: "))
        super()._validator(raw_input)
        
