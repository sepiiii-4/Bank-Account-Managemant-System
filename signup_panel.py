from tkinter import Tk , Label , Entry , Button , messagebox
from random import choice , randint

class SignUp:
    def __init__(self) :
        self.signup_window = Tk()
        self.signup_window.title("Create account")

        self.username_label = Label(self.signup_window , text= "Username :")
        self.username_label.grid(row= 0 , column= 0 , padx= 10 , pady= 10 , sticky= "w")

        self.username_entry = Entry(self.signup_window , width= 22)
        self.username_entry.grid(row= 0 , column= 1 , padx= (0,30) , pady= 10 , sticky= "w")

        self.password_label = Label(self.signup_window , text= "Password :")
        self.password_label.grid(row= 1 , column= 0 , padx= 10 , sticky= "w")

        self.password_entry = Entry(self.signup_window , width= 22)
        self.password_entry.grid(row= 1 , column= 1 , padx= (0,30) , sticky= "w")

        self.detail_label = Label(self.signup_window , text= "Password must be at least 8 characters." , fg= "blue")
        self.detail_label.grid(row= 2 , column= 0 , columnspan= 2 , padx=(10,30) , pady= 5 , sticky= "w")

        create_button = Button(self.signup_window , text= "Create" , command= self.sign_up)
        create_button.grid(row= 3 , column= 1 , padx= 10 , pady= (5,10) , sticky= "w")

    data_loc = "data.txt"
    
    def sign_up(self) :
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) == 0 or len(password) == 0 : 
            self.detail_label.config(text="Please write your username or password." , fg="red")
        elif len(password) < 8 :
            self.detail_label.config(text="Password must be at least 8 characters." , fg="red")
        else:
            with open(self.data_loc) as file :
                for data in file.readlines() :
                    new_list = data.replace("\n" , "").split(",")
                    try:
                        if username == new_list[1] :
                            message = messagebox.showerror("Error" , "This username has already existed .")
                            break
                    except IndexError :
                        pass   
                else :
                    # numbers = ["0",'1',"2","3","4","5","6","7","8","9"]
                    # user_id = ""
                    # is_correct = True
                    # while is_correct == True : 
                    #     for i in range (4) :
                    #         random_num = choice(numbers)
                    #         user_id += random_num
                    while 1 :
                        user_id = randint(1000 , 9999)
                        with open(self.data_loc) as file :
                            for data in file.readlines():
                                if data.startswith(str(user_id)) :
                                    continue
                            else :
                                break
                    with open(self.data_loc , mode= "a") as file :
                        new_data = f"{user_id},{username},{password},0.0\n"
                        file.write(new_data)
                        succed_message = messagebox.showinfo("New account" , "Your account succesfully opened.")  
            self.signup_window.destroy()                         
                                            
    def run(self):
        self.signup_window.mainloop()


