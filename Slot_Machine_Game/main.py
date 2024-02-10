import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]  * bet
            winning_lines.append(line + 1) 

    return winnings, winning_lines        







def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)    

    return columns   



def print_slots(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        
        print()        






def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: Rs. ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount entered should be greater than zero.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines



def get_bet():
    while True:
        bet = input("Enter the amount you want to bet: Rs. ")
        try:
            bet = float(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between Rs.{MIN_BET} - Rs.{MAX_BET}")
        except ValueError:
            print("Please enter a valid number.")
    return bet



def game_spin(balance):
    line = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * line
        if total_bet > balance:
            print(f"You do not have enough amount to bet, your current balance is Rs. {balance}")
            break
        else:
            break

    print(f"You are betting Rs.{bet} on {line} lines\nTotal bet is equal to Rs.{total_bet}")            
    slots = get_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings,winning_lines = check_winnings(slots,line,bet,symbol_value)
    print(f"You won Rs.{winnings}")
    print(f"You won lines:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is Rs.{balance}")
        if balance > 0:
            spin = input("Press enter to play (q to quit). ")
            if spin == "q":
                break
            balance += game_spin(balance)
        else:
            break

    print(f"You are left with Rs.{balance}")   
    print(f"Hello everyone")   

         


main()