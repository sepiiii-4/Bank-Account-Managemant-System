from tkinter import Frame, Label, Button, Entry, messagebox, END
from BusinessLogicLayer.user_business import CommonThings

class DepositFrame(Frame) :
    def __init__(self,main_view, window) :
        super().__init__(window)
        self.main_view = main_view
        self.user_business = CommonThings()

        self.back_button = Button(self, text= "Back", command= self.back)
        self.back_button.grid(row= 0, column= 0,padx= 10, pady= 10, sticky= "w")

        self.amount_label = Label(self, text= "Amount :")
        self.amount_label.grid(row= 1, column= 1, padx= 10, sticky= "w")

        self.amount_entry = Entry(self)
        self.amount_entry.grid(row= 1, column= 2, sticky= "w")

        self.dollar_sticker_label = Label(self, text= "$")
        self.dollar_sticker_label.grid(row=1, column= 3, padx= 2, sticky= "w")

        self.deposit_button = Button(self, text= "Deposit", state= "disabled", command= self.deposit)
        self.deposit_button.grid(row= 2, column= 2, pady= 10, sticky= "e")

        self.amount_entry.bind("<KeyRelease>", self.button_management)

    def set_current_user(self, current_user, frame_name) :
        self.current_user = current_user
        self.frame_name = frame_name

    def deposit(self) :
        amount = self.amount_entry.get()
        response = self.user_business.update_balance(amount, self.current_user.id, self.current_user.balance)
        message = messagebox.showinfo("Deposit", response.message)
        
        self.current_user.balance += response.data 
        self.amount_entry.delete(0, END)
        user_home = self.main_view.switch_frame(self.frame_name)
        user_home.set_current_user(self.current_user)

    def button_management(self, event) :
        amount = self.amount_entry.get()
        if amount :
            self.deposit_button.config(state= "normal")

    def back(self) :
        self.amount_entry.delete(0, END)
        self.main_view.switch_frame(self.frame_name)