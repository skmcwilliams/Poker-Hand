import random

def straight_hand():
    """function randomly draws 5 cards and identifies if the result in a straight or not"""
    straight = False
    count = 0
    while straight == False:
        # create suit and cards
        suits = ['♠', '♥', '♣', '♦']
        ranks = ['2','3','4','5','6','7','8','9', '10','J','Q', 'K', 'A']
        
        # convert face cards to numbers to rank
        ranks[-1] = 14 # ace high
        ranks[-2] = 13
        ranks[-3] = 12
        ranks[-4] = 11
        ranks = list(map(int,ranks)) # ensure all cars are integers

        # creat deck of cards
        deck = [[r,s] for s in suits for r in ranks]

        # hand is 5 randmonly drawn cards from deck
        hand = random.sample(deck, 5)

        # compare number of cards (suits don't matter in a straight)
        cards = [i[0] for i in hand]
        cards = list(map(int,cards))
        cards.sort() # sort to make identifying a straight easier

        # create list of differences
        diff = [y - x for x, y in zip(cards, cards[1:])]

        # check if all differences are equal to 1, if so then this is a straight and the program stops running
        if all(x == 1 for x in diff):
            count += 1
            print(cards)
            print('You have a straight after '+ str(count)+ ' hands!!')
            straight == True
            break

        # if all differenes are not equal to 1, then the hand is not a straight and the program continues to run
        else:
            count += 1
            print(cards)
            print('Hand ' + str(count) + ' is not a straight...\n')
            continue

straight_hand()
