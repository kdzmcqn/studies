import random

# global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'
         )
values = {'Two': 2,
          'Three': 3,
          'Four': 4,
          'Five': 5,
          'Six': 6,
          'Seven': 7,
          'Eight': 8,
          'Nine': 9,
          'Ten': 10,
          'Jack': 10,
          'Queen': 10,
          'King': 10,
          'Ace': 11
          }

playing = True

# class definitions


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []  # start with empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each card object's string
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# function definitions
# for taking bets


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Bet how many chips?'))

        except ValueError:
            print('sorry, must be a integer number')
        else:
            if chips.bet > chips.total:
                print("sorry, bet can't exceed ", chips.total)
            else:
                break


# function for taking hits


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# prompt to hit or stand


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('hit(h) or stand(s) ? ')
        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('player stands. dealer is playing.')
            playing = False

        else:
            print('sorry, please try again.')
            continue
        break


# function to display cards


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n')


def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand = ", player.value)

# * symbol is used to print every item in a collection
# sep='\n ' prints each item on a separate line
# print('', dealer.cards[1]) empty string and comma just to add space
"""commas to separate object being printed in each line
to concatenate, use + symbol, then call each Card object's
__str__ method explicitly w/

print(' ' + dealer.cards[1].__str__())
"""

# write functions to handle end game scenarios


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Payer wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Player and Dealer tie. it's a push")

# on the game

while True:
    print("welcome")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up player's chips
    player_chips = Chips()

    # prompt to take bet
    take_bet(player_chips)

    # show cards but keep dealer hidden
    show_some(player_hand, dealer_hand)

    while playing:  # from hit_or_stand function
        # prompt player to hit or stand
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # inform player of their chips total
    print("\nPlayer's winning stand at ", player_chips.total)

    # ask to play again
    new_game = input("new game, y or n? ")

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else:
        print("Thanks for playing!")
        break
