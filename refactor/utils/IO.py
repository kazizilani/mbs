class IO:
    def __init__(self, start, stop, *msg):
        self.msg = msg
        self.start = start
        self.stop = stop
        self.response = None

        #restricting access to avoid edit from anywhere else
        self.__validInput = False

    def _validator(self, response):
        try:
            if int(response) in range(self.start, self.stop+1):
                self.__validInput = True
                return response
        
            else:
                print("⭕ Selected Number Is Out Of Range")

        except:
           print("⭕ No Strings Allowed, Please Input A Number")
        
    def ask_input(self):
        while not self.__validInput:
            if self.msg:
                raw_input = str(input(f"{self.msg[0]}: "))
            else:
                raw_input = str(input("Select An Option: "))
        
            self.response = self._validator(raw_input)
        return self.response


        
    
