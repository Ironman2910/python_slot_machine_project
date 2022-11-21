

import random;

class Game:
    '''This is a 3 * 3 slot game'''
    ROWS=3
    COLUMNS=3
    WEIGHTED_SYMBOLS={'A':3,
                      'B':6,
                      'C':8,
                      'D':5}
    

    def __init__(self):
        print('*** Welcome to the Game! Try your luck and win $$$ amount! ***')
        self.balance = 0
        self.bet = 0
        self.generated = list()
        self.rows = 0
        self.bet_per_line = 0
        

    def sanity_check(self,dollars,category):
        
        if dollars.isdigit():
            if category == 'deposit':
                print(f'*** Dollar amount {dollars} is valid and is being deposited ***')
                return True
            if category == 'bet':
                print(f'*** You\'re about to bet on {dollars} lines ***')
                return True
        else:
            if category == 'deposit':
                print(f'*** You are trying to deposit invalid amount equal to ${dollars} ***')
                return False 
            if category == 'bet':
                print(f'*** Invalid choice -> {dollars} lines ***')
                return False
    
    def eligible(self,num_rows,bet_amt):
        if (int(num_rows)*int(bet_amt)) < self.balance:
            return True 
        return False
        
    def deposit(self):
        while True:
            dollars = input('Enter the amount you\'d like to Gamble with in USD! ')
            if self.sanity_check(dollars,'deposit'):
                self.balance+=int(dollars)
                print(f'*** Your Current balance is ${self.balance} ***')
            decision = input('*** Deposit again - Y/N? ***')
            if decision not in ('Y','N'):
                while True:
                    print('*** Invalid decision entered! ***')
                    decision = input('*** Enter Y to deposit or Enter N to decline *** ')
                    if decision == 'N' or decision == 'Y':
                        break
            if decision == 'N':
                print(f'*** Your Current balance is ${self.balance} ***')
                break
    
    def betAmount(self):
        while True:
            num_rows = input(f'*** Enter the num of lines you\'d like to bet on (1-{Game.ROWS}) *** ')
            if self.sanity_check(num_rows,'bet'):
                bet_amt = input(f'*** Enter the bet amount of your choice per line *** ')
                
                while True:
                    if self.eligible(num_rows,bet_amt):
                        self.bet = int(num_rows)*int(bet_amt)
                        self.rows = int(num_rows)
                        self.bet_per_line = bet_amt
                        print(f'*** You are betting a total of ${self.bet} ***')
                        break;
                    else:
                        xxx = int(num_rows)*int(bet_amt)
                        print(f'*** You\'re not eligible to bet ${xxx}, try again! ***')
                        bet_amt = input(f'*** Enter the bet amount of your choice per line *** ')
                break;

    def play(self):
        choices = ''
        for key in Game.WEIGHTED_SYMBOLS.keys():
            choices+=key*Game.WEIGHTED_SYMBOLS.get(key)
        choices = list(choices)

        for i in range(Game.ROWS):
            self.generated.append([])
            for j in range(Game.COLUMNS):
                self.generated[i].append(0)

            

        for i in range(Game.ROWS):
            for j in range(Game.COLUMNS):
                val = random.choice(choices)
                self.generated[i][j] = val
                choices.remove(val)

    def validate(self):
        flag = 1
        for i in range(0,self.rows):
            prev = self.generated[i][0]
            for j in range(0,Game.COLUMNS):
                if self.generated[i][j] != prev:
                    flag = 0
                    break 
                prev = self.generated[i][j]
            
            if flag == 0:
                break

        self.gen;
        if flag == 0:
            print('*** You have lost the game ***')
            self.balance = self.balance - self.bet 
        else:
            print('*** You have won! ***')
            self.balance += self.bet
        
        print(f'*** Your current balance is {self.balance} ***')

    @property
    def gen(self):
        for i in range(0,Game.ROWS):
            for j in range(0,Game.COLUMNS):
                if j == (Game.COLUMNS - 1):
                    print(self.generated[i][j],end='\n')
                else:
                    print(self.generated[i][j],end=' | ')
    



def main(game):
    while True:
        game.deposit()
        game.betAmount()
        game.play()
        game.validate()
        decision = input('*** Gamble again - Y/N? *** ')
        if decision == 'N':
            print(f'*** Your current walk away balance is {game.balance} ***')
            break;
        

game = Game()
main(game)


