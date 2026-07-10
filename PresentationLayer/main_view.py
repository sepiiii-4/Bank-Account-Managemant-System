from PresentationLayer.window import Window
from PresentationLayer.login import LoginFrame
from PresentationLayer.sign_up import SignUpFrame
from PresentationLayer.admin_home import AdminFrame
from PresentationLayer.detail import DetailFrame
from PresentationLayer.show_user import ShowUsersFrame
from PresentationLayer.user_home import UserHomeFrame
from PresentationLayer.transfer_funds import TransferFundsFrame
from PresentationLayer.deposit import DepositFrame

class MainView() :
    def __init__(self):
        window = Window()
        self.frames = {}

        self.add_frame("deposit", DepositFrame(self, window))
        self.add_frame("transfer_funds", TransferFundsFrame(self, window))
        self.add_frame("user", UserHomeFrame(self, window))
        self.add_frame("show_user", ShowUsersFrame(self, window))
        self.add_frame("detail", DetailFrame(self, window))
        self.add_frame("admin", AdminFrame(self, window))
        self.add_frame("signup", SignUpFrame(self, window))
        self.add_frame("login", LoginFrame(self, window))
        
        window.show()
    
    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, sticky="nsew")
    
    def switch_frame(self , name) :
        frame = self.frames[name]
        frame.tkraise()
        return frame
