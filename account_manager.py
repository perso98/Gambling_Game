# -*- coding: utf-8 -*-
import bcrypt
import csv

class AccountManager:
    
    def __init__(self, filepath = "accounts.csv"):
        self.filepath = filepath
    
    def create_account(self, login, password):
        logins_in_file = []
        with open(self.filepath) as file:
            lines = file.readlines()
            for line in lines:
                logins_in_file.append(line.split(",")[0])
            if login.lower() in logins_in_file:
                return 
            else:
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password.encode(), salt)
                with open(self.filepath, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([login, hashed_password.decode(), 0])
                    return {"login":login,"balance":0}
    
    
    def login(self, login, password):
        with open(self.filepath,'r') as file:
            lines = file.readlines()
            for line in lines:
                login_account, password_account, balance = line.split(',')
                if login.lower() == login_account.lower():
                    if bcrypt.checkpw(password.encode(), password_account.encode()):
                        balance = int(balance.replace("\n", ""))
                        return {"login":login, "balance":balance}
                    
    def update_balance(self, username, new_balance):
        updated_data = []
        found = False  
    
        with open(self.filepath, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    row[2] = str(new_balance) 
                    found = True
                updated_data.append(row)
    
        if found:
            with open(self.filepath, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
            print("Balans został zaktualizowany.")
            
       
        
    
    
