# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:30:10 2020

@author: Administrator
"""
from random import shuffle
from temp import Card
class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def rm_card(self):
        if self.cards == 0:
            return
        return self.cards.pop()
class Player:
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.card = None
