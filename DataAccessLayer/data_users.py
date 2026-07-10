import sqlite3
from Common.user import Users


class DataUsers :
    def __init__(self):
        self.database = "Data.db"

    # validate for login
    def get_user(self , username , password) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT  id,
                    first_name,
                    last_name,
                    username,
                    password,
                    balance,
                    card_number,
                    is_active,
                    role_id
            FROM    User
            where   username  =  ?
            AND     password  =  ?""" , [username,password]).fetchone()
            
            if data :
                user = Users(data[0] , data [1] , data[2] , data[3] , None , data[5] , data[6] , data[7] , data[8])
                return user
    
    # check whether a new user's info matches existing records
    def check_user(self, username) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT  id,
                    first_name,
                    last_name,
                    username,
                    password,
                    balance,
                    card_number,
                    is_active,
                    role_id
            FROM    User
            where   username  =  ?""" , [username]).fetchone()

            if data :
                return True
    
    # get all users for show in treeview
    def get_users(self, username):
        users_list = []
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT  id,
                    first_name,
                    last_name,
                    username,
                    password,
                    balance,
                    card_number,
                    is_active,
                    role_id
            FROM    User
            where   username  !=  ?""" , [username]).fetchall()

            for item in data :
                user = Users(item[0] , item [1] , item[2] , item[3] , None , item[5] , item[6] , item[7] , item[8])
                users_list.append(user)
        return users_list
    
    # add a new user to database
    def add_user(self, first_name, last_name, username, password, card_number) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            cursor.execute("""
            INSERT  INTO 
                    User (
                            first_name,
                            last_name,
                            username,
                            password,
                            card_number)
                    VALUES (
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""", [first_name, last_name, username, password, card_number])
            
            connection.commit()

    # update main info 
    def update_info(self,username ,first_name, last_name, password) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            cursor.execute("""
            UPDATE    User
            SET       first_name = ?,
                      last_name  = ?,
                      password   = ?
            WHERE     username   = ?""", [first_name, last_name, password, username])
            
            connection.commit()

    # change role by admin
    def change_role(self, id, role_id) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            cursor.execute("""
            UPDATE    User
            SET       role_id   = ?
            WHERE     id   = ?""", [role_id, id])
            
            connection.commit()

    # change activation by admin
    def change_activation(self, id, is_active):
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            cursor.execute("""
            UPDATE    User
            SET       is_active   = ?
            WHERE     id   = ?""", [is_active, id])

            connection.commit()
            
    def delete_account(self, id) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            cursor.execute("""
            DELETE FROM User
            WHERE  id  = ? """, [id])

            connection.commit()

    def transfer_funds(self, amount, card_number) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            user = cursor.execute("""
            SELECT  id,
                    balance,
                    is_active
            FROM    User
            Where   card_number = ?""", [card_number]).fetchone()
            
            if user :
                return user
            
    # for deposite to increase balance
    def update_balance(self, balance, id) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            cursor.execute("""
            UPDATE User
            SET    balance     = ?
            WHERE  id = ?""", [balance, id])

            connection.commit()

    # get all card number for validate
    def get_card_number(self) :
        with sqlite3.connect(self.database) as connection :
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT  card_number
            FROM    User""").fetchall()

            return data
           

            

 # if user[1] == 1 :
                #     cursor.execute("""
                #     UPDATE User
                #     SET    balance     = ?
                #     WHERE  card_number = ?""", [(user[0]+amount), card_number])
                    
                #     connection.commit()
                # else :
                #     return True
