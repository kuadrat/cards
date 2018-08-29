#!/usr/bin/python
import copy
import random

class Card() :
    """ The card object contains all the information a typical playing card 
    has, that is, rank and suit. While most cards can be represented just by 
    their ranks, (2, 3, ..., 10) some cards traditionally go by other names 
    (Jack, Queen, King, Ace), so a short and long representation are also 
    provided.
    """
    
    def __init__(self, rank=None, suit=None, name=None, shortname=None) :
        self.rank = rank
        self.suit = suit

        # Assign the rank of the card as its name, if nothing else is given
        if name is None :
            self.name = str(rank)
        else :
            self.name = name

        # Set the default shortname to the first letter of the cardname
        if shortname is None and name is not None :
            self.shortname = name[0]
        else :
            self.shortname = shortname

    def __str__(self) :
        if self.name is not None and self.suit is not None :
            return '{} of {}'.format(self.name, self.suit)
        else :
            return ('Card with rank ({}), name ({}) and '
                    'suit({}).').format(self.rank, self.name, self.suit)

    def __repr__(self) :
        return self.__str__()

class Deck() :
    """ A deck of cards. Contains a certain number of cards and allows the 
    most common deck operations like shuffling, sorting, dealing, etc.
    """

    drawn = []
    def __init__(self, cards=[]) :
        self.cards = cards
        # Retain a copy of all the cards for reference
        self.card_list = [copy.copy(card) for card in cards]
        self.size = len(self.cards)

        self.set_suit_order()

    def set_suit_order(self, suit_order=None) :
        """ Define in which case cards of same rank are to be ordered (both 
        in terms of strength in a game and literal order when sorting).
        If no *suit_order* is given, use the order in which the suits were 
        initially put into the deck.
        """
        # Get a list of all suits that appear in the deck
        all_suits = [card.suit for card in self.card_list]
        suits_in_deck = set(all_suits)

        if suit_order is None :
            # Use the order in which suits appear in the original card_list
            suit_order = []
            for suit in all_suits :
                if suit not in suit_order :
                    suit_order.append(suit)
        else :
            # Raise an error if the given *suit_order* doesn't
            if not suits_in_deck == set(suit_order) :
                message = ('Invalid suit_order. Make sure that each of the ' 
                           'following appears exactly once: \n')
                for suit in suits_in_deck :
                    message += '{}, '.format(suit)
                raise ValueError(message)

        self.suit_order = suit_order

    def shuffle_pile(self) :
        """ Shuffle the cards that have not yet been drawn (i.e. the cards 
        remaining in *self.cards*, while leaving *self.drawn* untouched). 
        """
        random.shuffle(self.cards)

    def shuffle_all(self) :
        """ Shuffle all cards belonging to this deck back into one pile 
        *self.cards*. 
        """
        self.cards += self.drawn
        self.drawn = []
        self.shuffle_pile()

    def draw(self, n=1) :
        """ Draw the top *n* cards from the draw pile *self.cards*. """
        cards = []
        for i in range(n) :
            card = self.cards.pop(0)
            cards.append(card)
        # Keep track of the drawn cards so they don't get lost
        self.drawn += cards
        return cards

# Create a standard 52 card poker set
cards = []
for suit in ['Hearts', 'Diamonds', 'Spades', 'Clubs'] :
    for rank in range(2, 11) :
        card = Card(rank=rank, suit=suit)
        cards.append(card)
    for rank,name in enumerate(['Jack', 'Queen', 'King', 'Ace']) :
        rank = rank + 11
        card = Card(rank=rank, suit=suit, name=name)
        cards.append(card)
french_deck = Deck(cards)

# Create a 36 card Swiss-German Deck
cards = []
for suit in ['Rosen', 'Schellen', 'Schilten', 'Eicheln'] :
    for rank in range(6, 10) :
        card = Card(rank=rank, suit=suit)
        cards.append(card)
    for rank,name in enumerate(['Banner', 'Under', 'Ober', 'König', 'Ass']) :
        rank = rank + 10
        card = Card(rank=rank, suit=suit, name=name)
        cards.append(card)
swiss_deck = Deck(cards)

# Create the 56 card Tichu deck
cards = []
for suit in ['Green', 'Blue', 'Black', 'Red'] :
    for rank in range(2, 11) :
        card = Card(rank=rank, suit=suit)
        cards.append(card)
    for rank,name in enumerate(['Jack', 'Queen', 'King', 'Ace']) :
        rank = rank + 11
        card = Card(rank=rank, suit=suit, name=name)
        cards.append(card)
dog = Card(rank=0, suit='Special', name='Dog', shortname='Dog')
mahjongg = Card(rank=1, suit='Special', name='Mahjongg')
phoenix = Card(rank=14.5, suit='Special', name='Phoenix')
dragon = Card(rank=15, suit='Special', name='Dragon', shortname='Dragon')
for card in [dog, mahjongg, phoenix, dragon] :
    cards.append(card)
tichu_deck = Deck(cards)

