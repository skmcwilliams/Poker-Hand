#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
As part of DePaul University's IPD 240 assigment 1_a
"""
from __future__ import print_function, division
from Card import Hand, Deck
import pandas as pd

class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """Returns True if hand has a two_of_a_kind"""
        self.rank_hist()
        for val in self.ranks.values():
            if val == 2:
                return True

    def has_two_pair(self):
        """Returns True if hand has a two_pair"""
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1
        if count >= 2:
            return True

    def has_three_of_a_kind(self):
        """Returns True if hand has a three_of_a_kind"""
        self.rank_hist()
        for val in self.ranks.values():
            if val == 3:
                return True

    def has_straight(self):
        """Returns True if hand has a straight"""
        # Set High Ace to low Ace
        self.rank_hist()
        if 1 and 14 in self.ranks.keys():
            self.ranks[14] = 1

        """Identify if difference of sequence of sorted cards is 1"""
        for card in self.cards:
            count = 0
            for i in range(5):
                if card.rank + i in self.ranks.keys():
                    count += 1
            if count == 5:
                return True

    def has_flush(self):
        """Returns True if the hand has a flush"""
        self.suit_hist()
        for val in self.suits.values():
            if val == 5:
                return True

    def has_full_house(self):
        """Returns True if hand has a full_house"""
        if self.has_pair() and self.has_three_of_a_kind():
            return True

    def has_four_of_a_kind(self):
        """Returns True if hand has a four_of_a_kind"""
        self.rank_hist()
        for val in self.ranks.values():
            if val == 4:
                return True

    def has_straight_flush(self):
        """Returns True if hand has straight flush, False otherwise"""
        if self.has_flush() and self.has_straight():
            return True

    def classify(self):
        """Classify hand and label hand according to highest rank of hand"""
        # create empty list of hands that are achieved, for each achieved hand, append to list
        classification = []

        # High Card means no hand is achieved, set as 0 due to lowest ranking
        classification.append({'High Card':0})

        if self.has_pair():
            classification.append({"Pair":1}) # Numbers represent ranking of each hand

        if self.has_two_pair():
            classification.append({'Two Pair':2})

        if self.has_three_of_a_kind():
            classification.append({'Three of a Kind':3})

        if self.has_straight():
            classification.append({'Straight':4})

        if self.has_flush():
            classification.append({'Flush':5})

        if self.has_full_house():
            classification.append({'Full House':6})

        if self.has_four_of_a_kind():
            classification.append({"Four of a Kind":7})

        if self.has_straight_flush():
            classification.append({"Straight Flush":8})

        for hands in classification:
            hand.label = max(hands, key=hands.get)

        return hand

if __name__ == '__main__':
    num_decks = int(input('How Many Decks to Shuffle?')) # Shuffle 1,000+ decks for highest accuracy
    num_hands = int(input('How Many Hands to Deal?')) # usually deal 7 hands
    total_hands = num_decks * num_hands
    prob_hist = {}

    for i in range(num_decks):
        deck = Deck()
        deck.shuffle()

    # deal the cards and classify the hands
        for i in range(num_hands):
            hand = PokerHand()
            deck.move_cards(hand, num_hands)
            hand.sort()
            hand.classify()
            # print(hand)
            # print(hand.label+'\n')
            # Creat histogram of each best hand
            prob_hist[hand.label] = prob_hist.get(hand.label, 0) + 1/total_hands*100
    # create dataframe of histogram
    table = pd.DataFrame.from_dict(prob_hist,orient='index', columns=['Best Hand Probability(%)'])
    print(table)
    print(f'\n Out of {total_hands} Total Hands')














