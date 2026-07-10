from tkinter import Frame, Button, Label, Entry, messagebox, END
from BusinessLogicLayer.user_business import Detail

class DetailFrame(Frame) :
    def __init__(self,main_view , window) :
        super().__init__(window)
        self.user_detail = Detail()
        self.main_view = main_view
        self.columnconfigure([0,1,2], weight= 1)

        self.header1 = Label(self, text= "Your info")
        self.header1.grid(row= 0 , column= 1 , padx= 10 , pady= 10)

        self.header2 = Label(self, text= "New info")
        self.header2.grid(row= 0 , column= 2 , padx= 10 , pady= 10)

        self.back_button = Button(self, text= "Back", command= self.back)
        self.back_button.grid(row= 0, column= 0, padx= 10, pady= 10, sticky= "w")

        self.first_name_label = Label(self, text= "", fg= "brown")
        self.first_name_label.grid(row= 1 , column= 1 , padx= 10 , sticky= "w")

        self.first_name_entry = Entry(self)
        self.first_name_entry.grid(row= 1 , column= 2 , padx= (0,20) , sticky= "ew")

        self.last_name_label = Label(self, text= "", fg= "brown")
        self.last_name_label.grid(row= 2 , column= 1 , padx= 10 , pady= 10 , sticky= "w")

        self.last_name_entry = Entry(self)
        self.last_name_entry.grid(row= 2 , column= 2 , padx= (0,20) , pady= 10 , sticky= "ew")

        self.password_label = Label(self, text= "Password : ********", fg= "brown")
        self.password_label.grid(row= 3 , column= 1 , padx= 10 , sticky= "w")

        self.password_entry = Entry(self)
        self.password_entry.grid(row= 3 , column= 2 , padx= (0,20) , sticky= "ew")

        self.change_button = Button(self, text= "Change", command= self.change)
        self.change_button.grid(row= 4, column= 2, padx= 20, pady= 10 , sticky= "e")

    def set_current_user(self, current_user, frame_name) :
        self.current_user = current_user
        self.frame_name = frame_name

        self.first_name_label.config(text= f"First name : {self.current_user.first_name}")
        self.first_name_entry.insert(0, self.current_user.first_name)

        self.last_name_label.config(text= f"Last name : {self.current_user.last_name}")
        self.last_name_entry.insert(0, self.current_user.last_name)

    def change(self) :
        password = self.password_entry.get()
        
        response = self.user_detail.validate(self.current_user.username, password)
        if not response :
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            
            if first_name and last_name :
                self.user_detail.update_info(self.current_user.username, first_name, last_name, password)
            else :
                message3= messagebox.showerror("Error", "Please fill all entries .")
                                        
            self.current_user.first_name = first_name
            self.current_user.last_name = last_name
            
            message2 = messagebox.showinfo("Update info", "Your information updated successfully .")

            self.first_name_entry.delete(0, END)
            self.last_name_entry.delete(0, END)
            self.password_entry.delete(0, END)

            admin_home = self.main_view.switch_frame(self.frame_name)
            admin_home.set_current_user(self.current_user)
            
        else :
            message1 = messagebox.showerror("Error",  "Your username or password is shorter than required ." )
            self.password_entry.delete(0, END)

    def back(self) :
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.main_view.switch_frame(self.frame_name)