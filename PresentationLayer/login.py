from tkinter import Frame , Label , Entry , Button , messagebox , END
from BusinessLogicLayer.user_business import Login

class LoginFrame(Frame) :
    def __init__(self ,main_view, window):
        super().__init__(window)

        self.main_view = main_view
        self.user_login = Login()

        self.columnconfigure(1 , weight= 1)

        self.header = Label(self , text= "Login Form")
        self.header.grid(row= 0 , column= 1 , padx= 0, pady= 10, sticky="w")

        self.username_label = Label(self, text="Username :")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password :")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = Entry(self, show= "*")
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.register_button = Button(self, text="Register", command= self.register)
        self.register_button.grid(row=3, column=1, pady=(0, 10), padx=(10, 20), sticky="w")

        self.login_button = Button(self, text="Login", command= self.login)
        self.login_button.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="e")        
    
    def login(self) :
        username = self.username_entry.get()
        password = self.password_entry.get()
     
        response = self.user_login.login(username, password)
        if not response.success :
            message =  messagebox.showerror("Error" , response.message)
        else :
            if response.data.role_id == 1 :
                admin_home = self.main_view.switch_frame("admin")
                admin_home.set_current_user(response.data)
            else :
                user_home = self.main_view.switch_frame("user")
                user_home.set_current_user(response.data)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
    
    def register(self) :
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.main_view.switch_frame("signup")
    
    


        


