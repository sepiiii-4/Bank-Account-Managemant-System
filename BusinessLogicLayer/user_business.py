from hashlib import md5
from random import choices
from DataAccessLayer.data_users import DataUsers
from Common.response import Response

class UserBusiness :
    def __init__(self):
        self.data_user = DataUsers ()

    def validate(self, username, password) :
        if len(username) < 3 or len (password) < 8 :
            return True
    
class Login(UserBusiness) :
    def __init__(self):
        super().__init__()

    def login (self , username, password : str) :
        if not self.validate( username, password ) :
            hashed_password = md5(password.encode()).hexdigest()
            user = self.data_user.get_user(username , hashed_password)
            if user :
                if user.is_active == 1 :
                    return Response(user, None, True)
                else :
                    return Response(None, "Your account is deactive .", False)
            else :
                return Response(None, "Your username or password is wrong .", False)
        else :
            return Response(None, "Your username or password is shorter than required .", False)
        
class SignUp(UserBusiness) :
    def __init__(self) :
        super().__init__()
        user_list = self.data_user.get_card_number()
        self.card_number_list = [ ]

        for item in user_list :
            for i in item :
                self.card_number_list.append(i)
    
    def user_validate(self, username, password) :
        if not self.validate(username, password) :
            user = self.data_user.check_user(username)
            if user :
                return Response(None, "Please change your username .", False)
            else :
                return Response(None, None, True)
        else :
            return Response(None, "Your username or password is shorter than required .", False)
        
    def insert_user(self, first_name, last_name, username, password : str):
        while 1:
            number = choices(range(1000,10000), k=4)
            card_number = " ".join([str(num) for num in number])
            if card_number in self.card_number_list :
                continue
            else :
                self.card_number_list.append(card_number)
                break
        hashed_password = md5(password.encode()).hexdigest()
        self.data_user.add_user(first_name, last_name, username, hashed_password, card_number)

class Detail(UserBusiness) :
    def __init__(self):
        super().__init__()
    
    def update_info(self,username, firstname, lastname, password : str):
        hashed_password = md5(password.encode()).hexdigest()
        self.data_user.update_info(username, firstname, lastname, hashed_password)

class ShowUser(UserBusiness):
    def __init__(self):
        super().__init__()
    
    def show_user (self, username) :
        user = self.data_user.get_users(username)
        return Response(user, None, True)
    
    def change_role_id(self, ids, role_id) :
        for id in ids :
            self.data_user.change_role(id, role_id)

    def active(self, ids) :
        for id in ids :
            self.data_user.change_activation(id, 1)
    
    def deactive(self, ids) :
        for id in ids :
            self.data_user.change_activation(id, 0)

class CommonThings(UserBusiness):
    def __init__(self):
        super().__init__()

    def delete_account(self, id) :
        self.data_user.delete_account(id)
        return Response(None, "Your account has been deleted .", True)
    
    def transfer_funds(self, amount, card_number, id, user_balance, user_card_number) :
        try :
            amount = int(amount)
        except ValueError :
            return Response(None, "Please write correct amount .", False)

        if user_card_number == card_number :
            return Response(None,  "You can't transfer to your own card number .", False)
        elif amount <= 0 :
            return Response(None, "Please write positive amount .", False)
        elif user_balance < amount :
            return Response(None, "Your account balance is insufficient for this transfer amount .", False)
        
        user = self.data_user.transfer_funds(amount, card_number)
        if user :
            if user[2] == 1 :
                self.data_user.update_balance((user[1]+amount), user[0])
                self.data_user.update_balance((user_balance-amount), id)
                return Response(amount, "This amount successfully transfered .", True)
            else :
                return Response(None, "This account is deactive .", False)
        else :
            return Response(None, "This card number doesn't exist .", False)
        
    def update_balance(self, amount, id, user_balance):
        try :
            amount = int(amount)
        except ValueError :
            return Response(None, "Please write correct amount .", False)
        if amount <= 0 :
            return Response(None, "Please write positive amount .", False)
        
        self.data_user.update_balance((amount+user_balance), id)
        return Response(amount, " Your balance successfully increased .", True)
    




    



    
    


            
        
            

        
