class Users :
    def __init__(self, id, first_name, last_name, username, password, balance, card_number, is_active, role_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.balance = balance
        self.card_number = card_number
        self.is_active = is_active
        self.role_id = role_id

    def get_fullname(self) :
        return f"{self.first_name} {self.last_name}"
    