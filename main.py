# -*- coding: utf-8 -*-
import bcrypt
import csv
from account_manager import AccountManager
from handlers import complete_login, handle_login, handle_registration, handle_game
import random

MIN_BET = 1
MAX_BET = 1000
MAX_PAYMENT = 20000
MIN_PAYMENT = 10
SYMBOLS = []
SYMBOLS = []
base_symbols = [
    {"fruit": '🍇', "price": 10, "win_multiply" : 2},
    {"fruit": '🍐', "price": 30, "win_multiply" : 5},
    {"fruit": '🍓', "price": 60, "win_multiply" : 10},
    {"fruit": '🍉', "price": 100, "win_multiply" : 20}
]

multiplicities = [10, 5, 3, 1]
for symbol, multiplicity in zip(base_symbols, multiplicities):
    SYMBOLS.extend([symbol] * multiplicity)


        


def main():
    manager = AccountManager()
    while True:
        action = input("Podaj co chcesz zrobić: "
                       "\n1- Utwórz nowe konto\n"
                       "2- Zaloguj się do konta\n"
                       "3- Wyjdź\n"
                       ">>> ")

        if action == "1":
            user = handle_registration(manager)
            if user:
                play_decision = input("Czy chcesz zacząć grać? (tak/nie): ")
                if play_decision.lower() == 'tak':
                    handle_game(user, SYMBOLS, MIN_BET, MAX_BET, MAX_PAYMENT, MIN_PAYMENT)
                    
        elif action == "2":
            user = handle_login(manager)
            if user:
                play_decision = input("Czy chcesz zacząć grać? (tak/nie): ")
                if play_decision.lower() == 'tak':
                    handle_game(user, SYMBOLS, MIN_BET, MAX_BET, MAX_PAYMENT, MIN_PAYMENT)
        
        elif action == "3":
            print("Dziękujemy za korzystanie z systemu.")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")
            
main()

        
        