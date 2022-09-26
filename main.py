''' ============================

Just hit run button and use the terminal to play.

============================= '''

import random

class BlackJack: 
    def __init__(self):
        self.pile = []
        self.hand = []
        self.croupier = []
        self.gameStatus = True
    
    def __create_pile(self):
        new_pile = []
        symbole = ["Hearts", "Diamonds", "Clubs", "Spades"]
        num = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for s in symbole:
            for n in num:
                new_pile.append([n, s])
        random.shuffle(new_pile)
        self.pile = new_pile

    def __get_card(self):
        return self.pile.pop()

    def __init_game(self):
        self.__create_pile()
        self.croupier.append(self.__get_card())
        self.hand.append(self.__get_card())
        self.hand.append(self.__get_card())

    def __load_value(self, hand):
        val = 0
        for card in hand:
            value = card[0]
            localVal = value
            if value == "J" or value == "Q" or value == "K": localVal = 10
            if value == "A":
                if val + 11 <= 21:
                    localVal = 11
                else: localVal = 1
            val += localVal
        return val

    def __init_message(self):
        return f"\n\nBlackJack Game !\n\nYour hand :\n{self.hand[0][0]} {self.hand[0][1]} & {self.hand[1][0]} {self.hand[1][1]} (value: {self.__load_value(self.hand)})\nDealer :\n{self.croupier[0][0]} {self.croupier[0][1]} (value: {self.__load_value(self.croupier)})"

    def __UI_message(self):
        playerCardsUI = ""
        croupierCardsUI = ""
        for card in self.hand:
            playerCardsUI += f"{card[0]} {card[1]} "
        for card in self.croupier:
            croupierCardsUI += f"{card[0]} {card[1]} "
        return f"\nYour hand :\n{playerCardsUI} (value: {self.__load_value(self.hand)})\nDealer :\n{croupierCardsUI} (value: {self.__load_value(self.croupier)})"

    def __check_end_game(self):
        if self.__load_value(self.hand) > 21:
            self.gameStatus = False
            return print("\nYou lose, your hand is over 21!")
        elif self.__load_value(self.hand) == 21:
            self.gameStatus = False
            return print("\nYou win, your hand is equal to 21!")
        elif self.__load_value(self.croupier) > 21:
            self.gameStatus = False
            return print("\nYou win, the hand of the dealer is over 21!")
        elif self.__load_value(self.croupier) == 21:
            self.gameStatus = False
            return print("\nYou lose, the hand of the dealer is equal to 21!")

    def player_stand(self):
        if self.__load_value(self.croupier) <= 11:
            self.croupier.append(self.__get_card())
        elif self.__load_value(self.croupier) <= 14:
            if random.randint(0, 2) == 1:
                self.croupier.append(self.__get_card())
        elif self.__load_value(self.croupier) <= 16:
            if random.randint(0, 3) == 1:
                self.croupier.append(self.__get_card())
        print(self.__UI_message())
        self.__check_end_game()
        if self.__load_value(self.hand) > self.__load_value(self.croupier):
            self.gameStatus = False
            return print("\nYou win, you beat the dealer!")
        else: 
            self.gameStatus = False
            return print("\nYou lose, the dealer beat you!")

    def player_hit(self):
        self.hand.append(self.__get_card())
        if self.__load_value(self.croupier) <= 11:
            self.croupier.append(self.__get_card())
        elif self.__load_value(self.croupier) <= 14:
            if random.randint(0, 2) == 1:
                self.croupier.append(self.__get_card())
        elif self.__load_value(self.croupier) <= 16:
            if random.randint(0, 3) == 1:
                self.croupier.append(self.__get_card())
        print(self.__UI_message())
        self.__check_end_game()

    def start_game(self):
        self.__init_game()
        print(self.__init_message())
        self.__check_end_game()

bj = BlackJack()
bj.start_game()
while bj.gameStatus:
    playerChoice = input("What's your choice, 'stand' or 'hit' ?")
    if(playerChoice == "stand"):
        bj.player_stand()
    elif(playerChoice == "hit"):
        bj.player_hit()
    else: print("Incorrect answer.")