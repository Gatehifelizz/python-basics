class Mpesa():
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
        

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount

            print(f"{amount} kes sent to {recipient} successfully")

        else:
            print("insufficient funds")


class Credo(Mpesa):
    def __init__(self, account_balance, phone_number, Id_number):
        super().__init__(account_balance, phone_number)
        self.Id_number = Id_number

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} kes  airtime bought successfully")
        else:
            print("insufficient funds")


class Business_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name

    def recieve_money(self, amount):
        self.account_balance += amount
        print(f"{amount} kes  received  successfully")

personal=Credo(500,713509121,26314195)
personal.send_money(300,87654321)
personal.buy_airtime(50)
biz=Business_Mpesa(2000,713509121,"onaires")
biz.recieve_money(3000)
biz.send_money(1500,87654321)



