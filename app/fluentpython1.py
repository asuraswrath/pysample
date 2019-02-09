# -*- coding: utf-8 -*-

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('jqka'.upper())
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank , suit) for rank in self.ranks
		                                 for suit in self.suits]

	def __len__(self):
		return len(self._cards)
	def __getitem__(self, position):
		return self._cards[position]

if __name__ == '__main__':
	beer_card = Card('7', 'diamonds')
	beer_card
	deck = FrenchDeck()
	print('len(deck) is {}'.formate(len(deck)))
	print('deck[0] is {}'.formate(deck[0]))
	print('deck[-1] is {}'.formate(deck[-1]))
	print('choice(deck) is {}'.formate(choice(deck)))
	print('deck[:3] is {}'.formate(deck[:3]))
	for card in deck:
		print('for in deck is{}'.formate(card))