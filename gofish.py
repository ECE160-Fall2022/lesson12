# Go Fish

from games import *
#from games import ask_number
#import games
#import games as g
from cards import *

"""
class GF_Card(Card):
    
"""

class GF_Deck(Deck):
    def do_nothing():
        return

class GF_Hand(Hand):

    def get_ranks(self):
        ranks = set()
        for card in self.cards:
            ranks.add(card.rank)
        return ranks
        

class GF_Player(GF_Hand):
    
    def __init__(self, name, score=0):
        super(GF_Player, self).__init__()
        self.name = name
        self.score = score

    def __str__(self):
        rep = ""
        rep += self.name + " (" + str(self.score) + " pts): "
        if self.cards:
            for card in self.cards:
                rep += str(card) + "\t"
        return rep

    def add_point(self):
        self.score += 1

class GF_Game(object):
    def __init__(self, names: list[str]):
        self.players : list[GF_Player] = []
        for name in names:
            self.players.append(GF_Player(name))

        self.deck = GF_Deck()
        self.deck.populate()
        self.deck.shuffle()
        print(self.deck)

    def __get_other_players_names(self, player):
        playerNames = []
        for p in self.players:
            if player.name != p.name:
                playerNames.append(p.name)
        return playerNames

    def __go_fish(self, player):
        print("Here are the possible cards: ", player.get_ranks())
        print(type(player.get_ranks()))
        rank = None
        while rank not in player.get_ranks():
            rank = input("Choose a rank to go fish: ")
        print("You chose: " + rank)

        print("Here are the players to steal from: ", self.__get_other_players_names(player))
        otherPlayerName = None
        while otherPlayerName not in self.__get_other_players_names(player):
            otherPlayerName = input("Choose a player to steal from: ")
        print("You're stealing " + rank + "'s from player " + otherPlayerName)
    
        otherPlayer = None    
        for p in self.players:
            if p.name == otherPlayerName:
                otherPlayer = p
        stoleCard = False
        stolenCards = []
        for i in range(len(otherPlayer.cards)):
            card = otherPlayer.cards[i]
            if rank == card.rank:
                print("You stole " + card.rank + card.suit + " from " + otherPlayer.name + ".")
                stolenCards.append(card)
                stoleCard = True
        for stolenCard in stolenCards:
            otherPlayer.give(stolenCard, player)
				
        if not stoleCard:
            print("No card to steal. Draw from the deck. Go fish!")
            self.deck.deal([player], 1)
        print(player)
        print()

    def __check_4_of_a_kind(self, player):
        for rank in player.get_ranks():
            count = 0
            cardsToRemove = []
            for card in player.cards:
                if rank == card.rank:
                    count += 1
                    cardsToRemove.append(card)
					
            if count == 4:
                player.add_point()

                for cardToRemove in cardsToRemove:
                    player.cards.remove(cardToRemove)


    def play(self):
        self.deck.deal(self.players, 5)
        for player in self.players:
            print(player)

        while self.deck.cards:
            for player in self.players:
                for p in self.players:
                    print(p)
                self.__go_fish(player)
                for p in self.players:
                    print(p)
                self.__check_4_of_a_kind(player)
                for p in self.players:
                    print(p)

def main():
    numPlayers = ask_number("How many players will be playing Go Fish? (2-6) ", 2, 6)

    playerNames = []
    for i in range(numPlayers):
        playerNames.append(input("Enter name: "))

    game = GF_Game(playerNames)
    game.play()

# turn based
# array of players
# player has cards

# loop through each player
# ask for a card rank
# ask for a player
# give card if available
# draw from the deck
# check 4 of a kind

main()
