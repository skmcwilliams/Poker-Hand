import random

def straight_hand():

    suits = ['♠', '♥', '♣', '♦']
    ranks = ['2','3','4','5','6','7','8','9', '10','J','Q', 'K', 'A']
    ranks[-1] = 14
    ranks[-2] = 13
    ranks[-3] = 12
    ranks[-4] = 11
    
    deck = [(r, s) for s in suits for r in ranks ]

    hand = random.sample(deck, 5)
    print(hand)
    cards = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    cards = [int(card) for card in cards]
    cards.sort()
    if cards[4] - cards[3] ==1 and cards[3] - cards[2] == 1 and cards [2] - cards[1] == 1 and cards[1] - cards[0] == 1:
        print(True)
        print('You have a straight!!')
    else:
        print(False)
        print('Hand is not a straight')    
straight_hand()