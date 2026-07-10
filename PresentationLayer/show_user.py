from tkinter import Frame, Button, END, messagebox
from tkinter.ttk import Treeview, Combobox
from BusinessLogicLayer.user_business import ShowUser

class ShowUsersFrame(Frame) :
    def __init__(self, main_view, window):
        super().__init__(window)
        self.main_view = main_view
        self.user_business = ShowUser()
        self.item_list = []

        self.columnconfigure(0, weight= 1)
        self.rowconfigure(2, weight= 1)

        self.back_button = Button(self, text= "Back", command= self.back)
        self.back_button.grid(row= 0, column= 0,padx= 10, pady= 10, sticky= "w")

        items = ["Admin", "User"]
        self.roll_combobox = Combobox(self, values= items, state= "readonly")
        self.roll_combobox.grid(row= 0, column= 0, padx= (10,0), pady=10)

        self.roll_button = Button(self, text= "Change", state= "disabled", command= self.change_roll)
        self.roll_button.grid(row= 1, column= 0, padx=(0,20), pady= 10)

        self.active_button = Button(self, text= "Active", state= "disabled", command= self.active)
        self.active_button.grid(row= 1, column= 0, padx= 10, sticky= "w")

        self.deactive_button = Button(self, text= "Deactive", state= "disabled", command= self.deactive)
        self.deactive_button.grid(row= 1, column= 0, padx= 10, sticky= "e")

        self.table = Treeview(self, columns= (1,2,3,4,5))
        self.table.grid(row= 2, column=0, padx= 10, pady= 10, sticky="nsew")

        self.table.heading("#0", text= "No")
        self.table.heading("#1", text= "First name")
        self.table.heading("#2", text= "Last name")
        self.table.heading("#3", text= "Username")
        self.table.heading("#4", text= "Activation")
        self.table.heading("#5", text= "Position")

        self.table.column("#0", width= 60, anchor= "w")
        self.table.column("#1", width= 100, anchor= "w")
        self.table.column("#2", width= 100, anchor= "w")
        self.table.column("#3", width= 100, anchor= "w")
        self.table.column("#4", width= 90, anchor= "w")
        self.table.column("#5", width= 90, anchor= "w")

        self.table.bind("<<TreeviewSelect>>", self.button_management)
        self.roll_combobox.bind("<<ComboboxSelected>>", self.button_management)

    def set_current_user(self, current_user) :
        self.current_user = current_user
        response = self.user_business.show_user(current_user.username)

        if response.success :
            self.load_table(response.data)
        else :
            message = messagebox.showerror("Error", "There isn't any user to show you .")
            self.main_view.switch_frame("admin")

    
    def load_table(self, user_list) :
        for item in self.item_list :
            self.table.delete(item)
        self.item_list.clear()

        row_number = 1
        for user in user_list :
            item = self.table.insert(
                    "",
                    END,
                    iid= user.id,
                    text= row_number,
                    values= [user.first_name, user.last_name,
                             user.username, "Active" if user.is_active == 1 else "Deactive",
                             "Admin" if user.role_id == 1 else "User"]
            )
            self.item_list.append(item)
            row_number+=1
    
    def change_roll(self) :
        selection = self.table.selection()
        roll = self.roll_combobox.get()
        self.user_business.change_role_id(selection, 1 if roll == "Admin" else 2)
        response = self.user_business.show_user(self.current_user.username)
        self.load_table(response.data)

    def active(self) :
        selection = self.table.selection()
        self.user_business.active(selection)
        response = self.user_business.show_user(self.current_user.username)
        self.load_table(response.data)

    def deactive(self) :
        selection = self.table.selection()
        self.user_business.deactive(selection)
        response = self.user_business.show_user(self.current_user.username)
        self.load_table(response.data)

    def button_management(self, event) :
        selection = self.table.selection()
        roll = self.roll_combobox.get()
        if selection :
            self.active_button.config(state= "normal")
            self.deactive_button.config(state= "normal")
        if selection and roll :
            self.roll_button.config(state= "normal")

    def back(self) :
        self.main_view.switch_frame("admin")