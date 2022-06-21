import random
from time import sleep

def values():
    return [x for x in range(1,14)]

def suits():
    return ["Hearts","Diamonds","Cloves",'Spades']

class Card:
    
    def __init__(self,value,suit):
        self.value = value
        self.suits = suit

    def __str__(self):
        return f"{self.value} of {self.suits}"
class Deck:
    def __init__(self):
        self.cards = [Card(value,suit) for value in values() for suit in suits()]

class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.total = 0
        self.score = 0
        
class Dealer:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.score = 0
        
class Blackjack:
    def __init__(self):
        self.current_player = None
        self.current_deck = None
        self.dealer = None
        
    def deal(self):
        random.shuffle(self.current_deck.cards)
        print("\nDealing....\n")
        sleep(1)
        for _ in range(2):
            self.hit()
            self.dealer.cards.append(self.current_deck.cards[-1])
            self.current_deck.cards.remove(self.dealer.cards[-1])
            
        self.current_player.total = self.current_player.cards[0].value + self.current_player.cards[1].value
        self.dealer.total = self.dealer.cards[0].value + self.dealer.cards[1].value
        print("Player Cards: ")
        for x in self.current_player.cards:
            print(x)
            sleep(1)
        print("\nDealer Cards:")
        sleep(1)  
        print(self.dealer.cards[1])
        print("*")

    def hit(self):
        self.current_player.cards.append(self.current_deck.cards[-1])
        self.current_deck.cards.remove(self.current_player.cards[-1])
        self.current_player.total += self.current_player.cards[-1].value
    
    def display_cards(self):
        print("\nPlayer Cards: ")
        for x in self.current_player.cards:
            print(x)
        print("\nDealer Cards:")
        for x in self.dealer.cards:
            print(x)
    
    def display_score(self):
        print("\nSCORES\n")
        print(f"Dealer:{self.dealer.score}\t {self.current_player.name}:{self.current_player.score}")        
    
    def run(self):
        new_dealer = Dealer()
        self.dealer = new_dealer
        deck = Deck()
        self.current_deck = deck
        
        print(
"""
Welcome To BLACKJACK!

Rules:
Anything Card Total over 21 is a Bust!
If player or dealer gets 21 on deal, whoever gets 21 wins.
If both players bust, Game Pushes
Dealer stands at 17
              
"""
            )
        
        player_name = input('Enter your name: ')
        player_name = Player(player_name)
        self.current_player = player_name
        
        while True:
            if len(self.current_deck.cards) < 10:
                new_deck = Deck()
                self.current_deck = new_deck        
            
            self.current_player.cards = []
            self.dealer.cards = []
            self.deal()
            
            if self.current_player.total == 21 and self.dealer.total != 21:
                
                print(f"Blackjack! {self.current_player.name} wins!")
                self.display_cards()
                self.current_player.score +=1
            elif self.current_player.total != 21 and self.dealer.total == 21:
                print("\nBlackjack! Dealer wins!")
                self.display_cards()
                self.dealer.score +=1
            elif self.current_player.total == 21 and self.dealer.total == 21:
                print("\nTwo blackjacks! Draw!")
                self.display_cards()
            elif self.dealer.total > 21 and self.current_player.total < 21:
                print(f"{self.current_player.name} wins! Dealer Bust")
                self.display_cards()
                self.current_player.score +=1
            elif self.dealer.total < 21 and self.current_player.total > 21:
                print(f"\nDealer wins! {self.current_player.name} Busts!")
                self.display_cards()
                self.dealer.score +=1
            elif self.dealer.total > 21 and self.current_player.total > 21:
                print("\nBoth Busts! Deal Pushes")
                self.display_cards()
            else:
                stand = False
                dealer_stand = False
                player_bust = False
                dealer_bust = False
                while not stand:
                    player_action = input("Would you like to [1] Hit, [2] Stand? ")
                    if player_action == "1":
                        self.hit()
                        print("\nHitting...\n")
                        sleep(1)
                        print(f"{self.current_player.name} gets {self.current_player.cards[-1]} ")
                        sleep(1)
                        print("\nPlayer Cards: ")
                        for x in self.current_player.cards:
                            print(x)
                        print("\nDealer Cards: ")
                        print(self.dealer.cards[1])
                        print("*")
                        if self.current_player.total > 21:
                            player_bust = True
                            stand = True
                        elif self.current_player.total == 21:
                            print("You hit 21!")
                            sleep(1)
                            stand = True
                    elif player_action == "2":
                        print("Standing...")
                        sleep(1)
                        stand = True
                    else:
                        print("Please enter [1] to Hit or [2] to Stand")
                if player_bust:
                    sleep(1)
                    print(f"\n{self.current_player.name} Busts! Dealer Wins!")
                    self.dealer.score += 1
                    sleep(1)
                    self.display_cards()
                    dealer_stand = True
                    dealer_bust = True
                
                while not dealer_stand:
                    dealer_stand = False
                    if self.dealer.total >= 17:
                        dealer_stand = True
                    else:
                        print("Dealer Cards: ")
                        for x in self.dealer.cards:
                            print(x)
                        print("\nDealer Hitting...")
                        sleep(1)
                        self.dealer.cards.append(self.current_deck.cards[-1])
                        print(f"Dealer gets {self.dealer.cards[-1]} ")
                        self.current_deck.cards.remove(self.dealer.cards[-1])
                        self.dealer.total += self.dealer.cards[-1].value
                        if self.dealer.total > 21:
                            dealer_stand = True
                            sleep(1)
                            print(f"\nDealer Busts! {self.current_player.name} Wins")
                            self.current_player.score += 1
                            self.display_cards()
                            dealer_bust = True
                            
                if not dealer_bust:
                    sleep(1)
                    print("Checking Results!")
                    sleep(1)   
                    self.display_cards()
                    if self.current_player.total > self.dealer.total:
                        print(f"{self.current_player.name} Wins!")
                        self.current_player.score += 1
                    elif self.current_player.total == self.dealer.total:
                        print("\nDealer Pushes!")
                    else:
                        print("\nDealer Wins!")
                        self.dealer.score +=1
                  
            self.display_score()
            quit_action = input(f"Would you like to continue {self.current_player.name}? [1] Yes [2] No ")
            if quit_action == "2":
                print("Thanks for Playing!")
                self.display_score()
                quit()
            
bj = Blackjack()
bj.run()           
            
        
    
        