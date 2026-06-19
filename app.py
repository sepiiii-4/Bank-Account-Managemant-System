from tkinter import Tk , Label , Entry , Button , messagebox
from tkinter.ttk import Treeview
from signup_panel import SignUp

_data_loc = "data.txt"



class Login :
    def __init__(self) :
        self.start_window = Tk()
        self.start_window.title("Start window")

        self.username_label = Label(self.start_window , text= "Username :")
        self.username_label.grid(row= 0 , column= 0 , padx= 10 , pady= 10 , sticky= "w")

        self.username_entry = Entry(self.start_window , width= 20)
        self.username_entry.grid(row= 0 , column= 1 , padx= (0,10) , pady= 10 , sticky= "w")

        self.password_label = Label(self.start_window , text= "Password :")
        self.password_label.grid(row= 1 , column= 0 , padx= 10 , sticky= "w")

        self.password_entry = Entry(self.start_window , width= 20)
        self.password_entry.grid(row= 1 , column= 1 , padx= (0,10) , sticky= "w")

        self.login_button = Button(self.start_window , text= "Login" , command= self.login)
        self.login_button.grid(row= 2 , column = 1 , padx= 10 , pady= 10 , sticky= "e")

        self.signup_button = Button(self.start_window , text= "Sign up" , command= lambda : SignUp().sign_up())
        self.signup_button.grid(row= 2 , column = 0 , padx= 10 , pady= 10 , sticky= "w")
    
    def login(self) :
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.user_data = []
        with open(_data_loc) as file :
            for data in file.readlines():
                new_list = data.replace("\n" , "").split(",")
                try :
                    if username == new_list[1] and password == new_list[2] :
                        self.user_data = new_list.copy()
                        app = Application ()
                        app.run()
                        break    
                except IndexError :
                    pass
            else :
                message = messagebox.showerror("Error" , "Your username or password is wrong .")
    def run(self) :
        self.start_window.mainloop()


class Application :        
    def __init__(self) : 
        login_page.start_window.destroy()
        self.user_panel = Tk()
        self.user_panel.title("User panel")

        self.detail_label = Label(self.user_panel , text= "Detail")
        self.detail_label.grid(row= 0 , column= 0 , columnspan= 2 , padx= 10 , pady= 10 , sticky="w")

        self.username_label = Label(self.user_panel , text= "Username :")
        self.username_label.grid(row= 1 , column= 0 , padx= 10 , sticky= "w")
        
        self.name_label = Label(self.user_panel , text= login_page.user_data[1])
        self.name_label.grid(row= 1 , column= 1 , padx= (0,10) , sticky= "w")

        self.password_label = Label(self.user_panel , text= "Password :")
        self.password_label.grid(row= 2 , column= 0 , padx= 10 , pady= 7 , sticky= "w")

        self.pass_label = Label(self.user_panel, text= "********" )
        self.pass_label.grid(row= 2 , column= 1 , padx= (0,10) , pady= 7 , sticky= "w")

        self.show_pass = Button(self.user_panel , text="Show" , command= self.show )
        self.show_pass.grid(row = 2 , column= 2 , pady = (0,7) , sticky = "w")

        self.id_label = Label(self.user_panel , text= "Id :")
        self.id_label.grid(row= 3 , column= 0 , padx= 10 , sticky= "w")

        self.num_label = Label(self.user_panel , text= login_page.user_data[0])
        self.num_label.grid(row= 3 , column= 1 , padx= (0,10) , sticky= "w")

        self.balance_label = Label(self.user_panel , text="Balance")
        self.balance_label.grid(row= 4 , column= 0 , padx= 10 , pady= 7 , sticky= "w")

        self.balance_int_label = Label(self.user_panel , text= f"{login_page.user_data[-1]} $")
        self.balance_int_label.grid(row= 4 , column= 1 , pady = 7 , sticky= "w")

        self.update_button = Button(self.user_panel , text= "Update" , command= self.update)
        self.update_button.grid(row= 4 , column= 2 , pady= 7 , sticky="w")

        self.balance_change = Button(self.user_panel , text= "Increase/decrease balance" ,command= lambda : ChangeBalance().run() )
        self.balance_change.grid(row= 2 , column= 5 , padx= (40,10) , sticky= "e")

        self.delete_account = Button(self.user_panel , text= "Delete account" , command= lambda : DeleteAccount.delete_account )
        self.delete_account.grid(row= 3 , column= 5 , padx= (40,10) , pady= 5 , sticky= "e")
     
        self.show_all_users = Button(self.user_panel , text= "Show all users" , command= lambda : ShowUsers().run())
        self.show_all_users.grid(row= 4 , column= 5 , padx= (40,10) , pady= (0,5) , sticky= "e")
    
    def update(self) :
        with open(_data_loc) as file :
            for data in file.readlines():
                if data.startswith(login_page.user_data[0]) :
                    new_list = data.replace("\n", "").split(",")
                    self.balance_int_label.config(text=f"{new_list[-1]} $ ")

    def show(self) :
        self.pass_label.config(text=login_page.user_data[2]) 
        
    def run (self) :
        self.user_panel.mainloop()


class ChangeBalance :
    def __init__(self) : 
        self.change_balance = Tk()
        self.change_balance.title("Change")

        self.amount_label = Label(self.change_balance , text= "Amount : ($)")
        self.amount_label.grid(row= 0 , column= 0 , padx= 10 , pady= 10 , sticky= "w")

        self.amount_entry = Entry(self.change_balance , width= 15)
        self.amount_entry.grid(row= 0 , column= 1 , padx= (0,10) , pady= 10 , sticky= "w")

        self.increase_button = Button(self.change_balance , text="Increase" , command= self.increase)
        self.increase_button.grid(row= 1 , column= 0 , padx= 10 , pady= (0,10) , sticky= "w")

        self.decrease_button = Button(self.change_balance , text= "Decrease" , command= self.decrease )
        self.decrease_button.grid(row= 1 , column= 1 , padx= 10 , pady= (0,10) , sticky= "e")

    def increase(self):
        amount = float(self.amount_entry.get())
        new_data = []
        with open(_data_loc) as file :
            for data in file.readlines():
                if data.startswith(login_page.user_data[0]) :
                    data = data.replace("\n" , "").split(",")
                    try :
                        amount+=float(data[-1])
                    except ValueError :
                        message = messagebox.showerror("Error" , "Type right value")
                    data[-1] = round(amount,2)
                    past_data = f"{data[0]},{data[1]},{data[2]},{data[3]}\n"
                    new_data.append(past_data)
                else :
                    new_data.append(data)

        with open(_data_loc , mode= "w") as file :
            file.writelines(new_data)
        increase_message = messagebox.showinfo("Money" , "Your account balance has been increased .")
        self.change_balance.destroy()

    def decrease(self):
        amount = float(self.amount_entry.get())
        new_data = []
        is_change = True
        with open(_data_loc) as file :
            for data in file.readlines():
                if data.startswith(login_page.user_data[0]) :
                    data = data.replace("\n" , "").split(",")
                    if amount <= float(data[-1]) :
                        try :
                            amount = float(data[-1]) - amount
                        except ValueError :
                            message = messagebox.showerror("Error" , "Type right value")
                        data[-1] = round(amount,2) 
                        past_data = f"{data[0]},{data[1]},{data[2]},{data[3]}\n"
                        new_data.append(past_data)
                    else :
                        is_change = False
                        balance_error = messagebox.showerror("Error" , "Your account balance is not sufficent for withdrawal .")
                else :
                    new_data.append(data)

        if is_change == True :
            with open(_data_loc , mode= "w") as file :
                file.writelines(new_data)
            increase_message = messagebox.showinfo("Money" , "Your account balance has been decreased .")
    
        self.change_balance.destroy()
    
    def run(self) :
        self.change_balance.mainloop()
        

class DeleteAccount :            
        def delete_account(self) :    
            new_data = []
            with open(_data_loc) as file :
                for data in file.readlines():
                    if data.startswith(login_page.user_data[0]) :
                        continue
                    else :
                        new_data.append(data)

            with open(_data_loc , mode= "w") as file :
                file.writelines(new_data)
            
            delete_message = messagebox.showinfo("Delete" , "Your account successfully deleted .")
            app = Application ()
            app.user_panel.destroy()


class ShowUsers :
    def __init__(self):
        self.users_tab = Tk()
        self.users_tab.title("Users")

        table = Treeview(self.users_tab , columns=(1,2,3,4))
        table.grid(row= 0 , column= 0 , padx= 10 , pady= 10 , sticky= "nswe")
        self.users_tab.grid_columnconfigure(0 , weight= 1)
        self.users_tab.grid_rowconfigure(0 , weight= 1)

        table.heading("#0" , text= "No")
        table.heading("#1" , text= "Id")
        table.heading("#2" , text= "Username")
        table.heading("#3" , text= "Password")
        table.heading("#4" , text= "Balance ($)")

        with open(_data_loc) as file :
            row_number = 1
            for data in file.readlines():
                new_list = data.replace("\n" , "").split(",")
                table.insert("" , "end" , text= str(row_number) , values= (new_list[0] , new_list[1] , "********" , new_list[3]))
                row_number+=1

    def run(self) :    
        self.users_tab.mainloop()

        

login_page = Login ()
login_page.run()
    
    
        



