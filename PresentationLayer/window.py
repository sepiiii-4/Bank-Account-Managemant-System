from tkinter import Tk

class Window(Tk) :
    def __init__(self):
        super().__init__()

        self.geometry("630x400")
        self.title("Bank Application")
        self.rowconfigure(0 , weight=1)
        self.columnconfigure(0 , weight=1)
        
    def show(self) :
        self.mainloop()