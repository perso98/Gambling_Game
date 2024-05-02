import random
import time
from account_manager import AccountManager
balance_manager = AccountManager()
def complete_login(user_info):
    if user_info:
        print(f"Zalogowano pomyślnie {user_info['login'].title()}. Twój balans to: {user_info['balance']} PLN")
        return True  # Zwróć True, oznaczające sukces
    else:
        print("Niepoprawny login lub hasło. Spróbuj ponownie.\n")
        return False  # Zwróć False, oznaczające brak sukcesu
    
def handle_login(manager):
    login_success = False
    while not login_success:
        login = input("Podaj login do konta: ")
        password = input("Podaj hasło do konta: ")
        user_info = manager.login(login, password)
        login_success = complete_login(user_info)
        if login_success:
            return user_info
    
def handle_registration(manager):
    registration_success = False
    while not registration_success:
        login = input("Podaj login do nowego konta: ")
        password = input("Podaj hasło nowego do konta: ") 
        user_info = manager.create_account(login, password)
        registration_success = complete_login(user_info)
        if registration_success:
            return user_info
def depozyt(MAX_PAYMENT, MIN_PAYMENT):
    while True:
        kwota = input("Podaj kwotę, którą chcesz wpłacić \nPLN >>> ")
        if kwota.isdigit():
            kwota = int(kwota)
            if kwota > MAX_PAYMENT or kwota < MIN_PAYMENT:
                print(f"Maksymalna wpłata to {MAX_PAYMENT} a minimalna to: {MIN_PAYMENT} PLN")
            elif kwota > 0:
                print("Poczekaj chwile dokonujemy przelewu...")
                time.sleep(3)
                print(f"Wpłaciłes pomyslnie {kwota} PLN")
                time.sleep(3)
                return kwota
            else:
                print("Kwota musi być więszka od 0...")
        else:
            print("Kwota musi być liczbą...")
            
def handle_game(user_info, SYMBOLS, MIN_BET, MAX_BET, MAX_PAYMENT, MIN_PAYMENT):
    rounds = 0
    while True:
        if rounds > 0:
            print("Sprawdzamy twoje saldo na koncie...")
        if user_info['balance'] == 0:
            print("Nie masz środków na koncie")
            user_info['balance'] += depozyt(MAX_PAYMENT, MIN_PAYMENT)
            balance_manager.update_balance(user_info['login'], user_info['balance'])
        
        bet = input(f"Ile chcesz postawić {user_info['login'].title()}? Twoje saldo to {user_info['balance']} PLN\n>>>")
        
        if bet.isdigit():
            bet = int(bet)
            if bet < MIN_BET or bet > MAX_BET:
                print(f"Kwota zakładu musi być między {MIN_BET} PLN a {MAX_BET} PLN.")
            elif bet > user_info['balance']:
                print("Nie masz wystarczających środków na koncie...")
                depozyt_price = depozyt(MAX_PAYMENT, MIN_PAYMENT)
                user_info['balance'] += depozyt_price
                balance_manager.update_balance(user_info['login'], user_info['balance'])
            else:
                print(f"Grasz za {bet} PLN...")
                result = [random.choice(SYMBOLS) for _ in range(3)]
                for fruit in result:
                    time.sleep(2)
                    print(fruit['fruit'])
                time.sleep(1)
                if all(fruit['fruit'] == result[0]['fruit'] for fruit in result):
                    win = bet * result[0]['price']
                    print(f"🥳🥳🥳 Wygrałeś {win} PLN")
                    user_info['balance'] += win
                    balance_manager.update_balance(user_info['login'], user_info['balance'])
                    time.sleep(2)
                else:
                    print(f"😭😔💔 Przegrałeś {bet} PLN")
                    user_info['balance'] -= bet
                    balance_manager.update_balance(user_info['login'], user_info['balance'])
                    time.sleep(2)
        else:
            print("Wpisane dane nie są liczbą. Wpisz liczbę w formacie cyfrowym.")

        rounds += 1
   
        