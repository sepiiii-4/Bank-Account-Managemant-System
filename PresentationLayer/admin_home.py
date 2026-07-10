from tkinter import Frame, Button, Label, messagebox
from BusinessLogicLayer.user_business import UserBusiness, CommonThings


class AdminFrame(Frame) :
    def __init__(self,main_view, window) :
        super().__init__(window)
        self.main_view = main_view
        self.user_business = UserBusiness()
        self.user_work = CommonThings()

        self.columnconfigure(0, weight= 1)

        self.header = Label(self, text="", fg= "sienna")
        self.header.grid(row= 0 ,column= 0 ,padx= 10 ,pady= 10)

        self.show_users_button = Button(self, text= "Show Users", command= self.show_user)
        self.show_users_button.grid(row= 1,column= 0 ,padx= 10 ,pady= 10 ,sticky= "w")

        self.deposit_button = Button(self, text= "Deposit", command= self.deposit)
        self.deposit_button.grid(row= 2, column= 0, padx= 10, sticky= "w")
        
        self.change_detail_button = Button(self, text= "Change Detail", command= self.change_detail)
        self.change_detail_button.grid(row= 1,column= 0 ,padx= 10 ,pady= 10 ,sticky= "e")

        self.transfer_funds_button = Button(self, text= "Transfer funds", command= self.transfer_funds)
        self.transfer_funds_button.grid(row= 2, column= 0, padx= 10, sticky= "e")
        
        self.logout_button = Button(self, text= "Log Out", command= self.logout)
        self.logout_button.grid(row= 2, column= 0, padx= 10, pady= 10)

        self.detail_label = Label(self, text= "Detail ")
        self.detail_label.grid(row= 3, column=0 ,padx= 10, pady= 10, sticky= "w")

        self.delete_account_button = Button(self, text= "Delete account", command= self.delete_account)
        self.delete_account_button.grid(row= 3, column= 0, padx= 10, pady=(0,10), sticky= "e")

        self.cardnumber_label = Label(self, text= "Card number :")
        self.cardnumber_label.grid(row= 4, column=0, padx= (10,5), sticky= "w")

        self.cardnumber_value_label = Label(self, text= "")
        self.cardnumber_value_label.grid(row= 5, column= 0, padx= (30,0), pady= 10, sticky= "w")

        self.balance_label = Label(self, text= "Balance :")
        self.balance_label.grid(row= 6, column= 0, padx= 10, sticky= "w")

        self.balance_value_label = Label(self, text= "")
        self.balance_value_label.grid(row= 7, column= 0, padx= (30,0), pady= 10, sticky= "w")

    def set_current_user(self, current_user) :
        self.current_user = current_user 

        self.header.config(text=f"Welcome {self.current_user.get_fullname()} to your panel .")
        self.cardnumber_value_label.config(text= self.current_user.card_number)
        self.balance_value_label.config(text=f"{(self.current_user.balance):,} $")

    def change_detail(self) :
        main_view = self.main_view.switch_frame("detail")
        main_view.set_current_user(self.current_user, "admin")
    
    def logout(self) :
        self.main_view.switch_frame("login")

    def show_user(self) :
        show_user_frame = self.main_view.switch_frame("show_user")
        show_user_frame.set_current_user(self.current_user)

    def delete_account(self) :
        message= messagebox.askyesno("Delete account", "Are you sure to want to delete your account ?")
        if message :
            response = self.user_work.delete_account(self.current_user.id)
            message2 = messagebox.showinfo("Delete account", response.message)
            self.main_view.switch_frame("login")

    def deposit(self) :
        transfer_frame = self.main_view.switch_frame("deposit")
        transfer_frame.set_current_user(self.current_user, "admin")

    def transfer_funds(self) :
        transfer_frame = self.main_view.switch_frame("transfer_funds")
        transfer_frame.set_current_user(self.current_user, "admin")
        


