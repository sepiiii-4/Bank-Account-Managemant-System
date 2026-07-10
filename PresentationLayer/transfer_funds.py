from tkinter import Frame, Label, Entry, Button, messagebox, END
from BusinessLogicLayer.user_business import CommonThings

class TransferFundsFrame(Frame) :
    def __init__(self, main_view, window):
        super().__init__(window)
        self.main_view = main_view
        self.user_business = CommonThings()

        self.back_button = Button(self, text= "Back", command= self.back)
        self.back_button.grid(row= 0, column= 0,padx= 10, pady= 10, sticky= "w")

        self.card_number_label = Label(self, text= "To :")
        self.card_number_label.grid(row= 1, column= 1, padx= (0,10), sticky= "w")

        self.card_number_entry = Entry(self, width= 20)
        self.card_number_entry.grid(row= 1, column= 2, pady= 10, sticky= "w")

        self.amount_label = Label(self, text= "Amount :")
        self.amount_label.grid(row= 2, column= 1, padx= (0,10), sticky= "w")

        self.amount_entry = Entry(self)
        self.amount_entry.grid(row= 2, column= 2, sticky= "ew")

        self.transfer_button = Button(self, text= "Transfer", state= "disabled", command= self.transfer)
        self.transfer_button.grid(row= 3, column= 1, pady= 10, sticky= "e")

        self.dollar_sticker_label = Label(self, text= "$")
        self.dollar_sticker_label.grid(row=2, column= 3, padx= 2, sticky= "w")

        self.card_number_entry.bind("<KeyRelease>", self.format_card_number)
        self.card_number_entry.bind("<KeyRelease>", self.button_management, add= "+")
        self.amount_entry.bind("<KeyRelease>", self.button_management)

    def set_current_user(self, current_user, frame_name) :
        self.current_user = current_user
        self.frame_name= frame_name

    def transfer(self) :
        card_number = self.card_number_entry.get()
        amount = self.amount_entry.get()
        
        response = self.user_business.transfer_funds(amount, card_number, self.current_user.id, self.current_user.balance, self.current_user.card_number)
        if response.success :
            message = messagebox.showinfo("Transfer", response.message)
            self.current_user.balance-= response.data
            self.card_number_entry.delete(0, END)
            self.amount_entry.delete(0, END)
            user_home = self.main_view.switch_frame(self.frame_name)
            user_home.set_current_user(self.current_user)
        else :
            message2 = messagebox.showerror("Error", response.message)
        

    def button_management(self, event) :
        card_number = self.card_number_entry.get()
        amount = self.amount_entry.get()

        if card_number and amount :
            self.transfer_button.config(state= "normal")

    def format_card_number(self, event) :
        text = self.card_number_entry.get().replace(" ","")
        if len(text) > 16 :
            text = text[0:16]
        text = " ".join(text[i:i+4] for i in range(0,len(text),4))
        self.card_number_entry.delete(0, END)
        self.card_number_entry.insert(0, text)
        self.card_number_entry.icursor(END)
        
        if len(text) == 19 :
            self.amount_entry.focus_set()
  
    def back(self) :
        self.card_number_entry.delete(0, END)
        self.amount_entry.delete(0, END)
        self.main_view.switch_frame(self.frame_name)