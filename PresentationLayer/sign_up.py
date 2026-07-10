from tkinter import Frame, Label, Entry, Button, messagebox, END
from BusinessLogicLayer.user_business import SignUp


class SignUpFrame(Frame):
    def __init__(self, main_view, window) :
        super().__init__(window)

        self.main_view = main_view
        self.signup_user = SignUp()

        self.columnconfigure(1, weight=1)
        
        self.header = Label(self, text= "Signup Form")
        self.header.grid(row= 0 , column= 1 , padx= 10 , pady= 10 , sticky= "w")
        
        self.back_button= Button(self, text= "Back", command= self.swich_login_frame)
        self.back_button.grid(row= 0, column= 0, padx=(10,0), pady= 10, sticky= "w")

        self.first_name_label = Label(self, text= "First name :")
        self.first_name_label.grid(row= 1 , column= 0 , padx= 10 , pady= 10 , sticky= "w")

        self.first_name_entry = Entry(self)
        self.first_name_entry.grid(row= 1 , column= 1 , padx= (0,20) , sticky= "ew")

        self.last_name_label = Label(self, text= "Last name :")
        self.last_name_label.grid(row= 2 , column= 0 , padx= 10 , sticky= "w")

        self.last_name_entry = Entry(self)
        self.last_name_entry.grid(row= 2 , column= 1 , padx= (0,20) , pady= 10 , sticky= "ew")

        self.username_label = Label(self, text= "Username :")
        self.username_label.grid(row= 3 , column= 0 , padx= 10 , pady= 10 , sticky= "w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row= 3 , column= 1 , padx= (0,20) , sticky= "ew")

        self.password_label = Label(self, text= "Password :")
        self.password_label.grid(row= 4 , column= 0 , padx= 10 , sticky= "w")

        self.password_entry = Entry(self, show= "*")
        self.password_entry.grid(row= 4 , column= 1 , padx= (0,20) , pady= 10 , sticky= "ew")

        self.signup_button = Button(self, text= "Sign Up" , command= self.sign_up)
        self.signup_button.grid(row= 5 , column= 1 , padx= 20 , pady=(0,10) , sticky= "e" )

    def sign_up(self) :
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        response = self.signup_user.user_validate(username, password)
        if not response.success :
            message1 = messagebox.showerror("Error", response.message)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
        else :
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()

            self.signup_user.insert_user(first_name, last_name, username, password)
            message2 = messagebox.showinfo("Sign Up", "Your account has been created successfully")
            self.swich_login_frame()

    def swich_login_frame(self) :
        self.main_view.switch_frame("login")





