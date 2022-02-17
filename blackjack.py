"""
File: blackjack.py
This module defines the Blackjack, Player, and Dealer classes.
"""

'**IN PROGRESS**'


from breezypythongui import EasyFrame
from tkinter import PhotoImage
from cards import Deck, Card

class Player(object):
    """This class represents a player in
    a blackjack game."""

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        """Returns string rep of cards and points."""
        result = ", ".join(map(str, self.cards))
        result += "\n  " + str(self.getPoints()) + " points"
        return result

    def hit(self, card):
        self.cards.append(card)

    def getPoints(self):
        """Returns the number of points in the hand."""
        count = 0
        for card in self.cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        # Deduct 10 if Ace is available and needed as 1
        for card in self.cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        """Dealt 21 or not."""
        return len(self.cards) == 2 and self.getPoints() == 21 


class Dealer(Player):
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        """Initial state: show one card only."""
        Player.__init__(self, cards)
        self.showOneCard = True

    def __str__(self):
        """Return just one card if not hit yet."""
        if self.showOneCard:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        """Add cards while points < 17,
        then allow all to be shown."""
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())

class Blackjack(EasyFrame):

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])
        EasyFrame.__init__(self, title = "BlackJack GUI")
        self.setSize(220, 320)
        """Add labels and buttons to the view"""
        self.playercardLabel1 = self.addLabel("test", row = 0,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = "5")
        self.playercardLabel2 = self.addLabel("test", row = 0,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = "5")
        self.playercardLabel3 = self.addLabel("test", row = 0,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = "5")
        self.playercardLabel4 = self.addLabel("test", row = 0,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = "5")
        self.playercardLabel5 = self.addLabel("test", row = 0,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = "5")
        self.dealercardLabel1 = self.addLabel("test", row = 1,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = 5)
        self.dealercardLabel2 = self.addLabel("test", row = 1,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = 5)
        self.dealercardLabel3 = self.addLabel("test", row = 1,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = 5)
        self.dealercardLabel4 = self.addLabel("test", row = 1,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = 5)
        self.dealercardLabel5 = self.addLabel("test", row = 1,
                                       column = 1,
                                       sticky = "NSEW",
                                       columnspan = 5)
        self.stateArea = self.addTextArea("test", row = 1, column = 0,
                                        columnspan = 1, width = 0,
                                        height = 0)
        self.hitButton = self.addButton(row = 10, column = 1,
                                         text = "Hit",
                                         command = self.play)
        self.standButton = self.addButton(row = 10, column = 2,
                                         text = "Stand",
                                         command = self.play)
        self.addButton(row = 10, column = 3,
                       text = "New game",
                       command = self.newGame)
        #self.refreshImages()

    def play(self):
        print("Player:\n", self.player)
        print("Dealer:\n", self.dealer)
        while True:
            choice = input("Do you want a hit? [y/n]: ")
            if choice in ("Y", "y"):
                self.player.hit(self.deck.deal())
                points = self.player.getPoints()
                print("Player:\n", self.player)
                if points >= 21:
                    break
            else:
                break
        playerPoints = self.player.getPoints()
        if playerPoints > 21:
            print("You bust and lose")
        else:
            self.dealer.hit(self.deck)
            print("Dealer:\n", self.dealer)
            dealerPoints = self.dealer.getPoints()
            if dealerPoints > 21:
                print("Dealer busts and you win")
            elif dealerPoints > playerPoints:
                print("Dealer wins")
            elif dealerPoints < playerPoints and playerPoints <= 21:
                print("You win")
            elif dealerPoints == playerPoints:
                if self.player.hasBlackjack() and not self.dealer.hasBlackjack():
                    print("You win")
                elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
                    print("Dealer wins")
                else:
                    print("There is a tie")
        
    def hit(self):
        self.hitbutton = True
        self.play()


    def stand(self):
        self.standButton = True
        self.play()

    def newGame(self):
        """Create a new craps game and updates the view."""
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])
        self.stateArea('')
        self.hitButton["state"] = "normal"
        self.standButton["state"] = "normal"
        """
        self.v1 = 1
        self.v2 = 1
        self.player.winner = self.player.loser = False
        self..setText('')
        self.rollButton["state"] = "normal"
        self.refreshImages()
        """

    def refreshImages(self):
        
        fileName1 = "Card/" + str(self.v1) + ".gif"
        fileName2 = "Card/" + str(self.v2) + ".gif"
        self.image1 = PhotoImage(file = fileName1)
        self.playercardLabel1["image"] = self.image1
        self.image2 = PhotoImage(file = fileName2)
        self.playercardLabel2["image"] = self.image2
        
def main():
    """Instantiate the model and play the game."""
    game = Blackjack()
    game.play()

if __name__ == "__main__":
    main()
  
