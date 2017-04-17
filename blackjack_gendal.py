from random import choice

blackjack = 21
jack = 10
queen = 10
king = 10
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]
players_cards = []
dealers_cards = []
blackjack_winners = []
busters = []
dealer_bust_dummy = 0

print 'Hello and welcome to a game of BlackJack!'
num_players = int(raw_input('Please enter the number of players (User will control all players except Dealer) '))


def initial_deal_cards(number_of_players):              # This first adds the correct number of lists
    for i in range(num_players):                        # you will need depending on how many players are chosen by the user
        players_cards.append([])
    for j in range(2):                                  # This adds 2 random cards to each player
        for h in players_cards:
            h.append(choice(cards))
        dealers_cards.append(choice(cards))
    print players_cards


def check_aces_players(cards):
    for i in range(len(players_cards)):
        if 1 in players_cards[i] and ((sum(players_cards[i]) + 10) == 21):
            players_cards[i].append(10)
            blackjack_winners.append([i, players_cards[i]])
        elif 1 in players_cards[i] and (17 <= (sum(players_cards[i]) + 10) <= 20 ):
            players_cards[i].append(10)


def check_aces_dealer(dealers_cards):
    if 1 in dealers_cards:
        if 17 <= (sum(dealers_cards) + 10) <= 20:
            dealers_cards.append(10)
            print "DEALER FINISHED HAND WITH A {}".format(sum(dealers_cards))
            dealers_cards.append(0)
        elif sum(dealers_cards) + 10 == 21:
            dealers_cards.append(10)
            print "DEALER GOT BLACKJACK!"


def check_player_cards():
    for i in range(len(players_cards)):
        if sum(players_cards[i]) == 21:
            print 'Player {} GOT BLACKJACK!'.format(i)
        elif sum(players_cards[i]) > 21:
            print 'Player {} BUSTS'.format(i)

def check_dealer_cards():
    if sum(dealers_cards) == 21:
        print 'DEALER GOT BLACKJACK'
    elif d_total > 21:
        print 'DEALER BUSTS'
    elif 17 <= d_total <= 21:
        print 'DEALER FINISHED HAND WITH A {}'.format(sum(dealers_cards))
    else:
        print 'Dealer has a {}'.format(sum(dealers_cards))

def hit_or_stick(players_cards):   # Players who got blackjack (21) with the first two cards have already been removed from [players_cards] list.
    for i in range(len(players_cards)):
        active = True
        while active == True:
            if sum(players_cards[i]) == 21:
                active = False
            else:
                print 'Player {} : hit or stick? Your cards are {}, a total of {} and the dealer shows {}. '.format(i, players_cards[i], sum(players_cards[i]), dealers_cards)
                h_or_s = raw_input()
                if h_or_s == 'hit':
                    players_cards[i].append(choice(cards))
                    print 'You received a {} for a total of {}'.format(players_cards[i][-1], sum(players_cards[i]))
                    if 1 in players_cards[i] and (17 <= (sum(players_cards[i]) + 10) <= 21):          #first check to see if last element appended was an ace and if that would give player sum between 17 and 21
                        players_cards[i].append(10)
                    elif sum(players_cards[i]) == 21:
                        print 'PLAYER {} GOT BLACKJACK!'.format(i)
                        blackjack_winners.append(['Player', i, 'Cards', players_cards[i]])
                        active = False
                    elif sum(players_cards[i]) > 21:
                        print 'Player {} BUSTS'.format(i)
                        players_cards[i].append(0)
                        active = False
                    elif sum(players_cards[i]) < 21:
                        print 'Player {} has a {}'.format(i, sum(players_cards[i]))
                else:
                    print 'Player {} finishes with a {}'.format(i, sum(players_cards[i]))
                    active = False
def deal_dealer():
    active = True
    if 0 in dealers_cards:
        pass
    else:
        while active == True:
            print 'Dealer has {} and a total of {}'.format(dealers_cards, sum(dealers_cards))
            if sum(dealers_cards) < 17:
                dealers_cards.append(choice(cards))
            elif 17 <= sum(dealers_cards) <= 20:
                print 'Dealer finished with {} and a total of {}'.format(dealers_cards, sum(dealers_cards))
                active = False
            elif sum(dealers_cards) == 21:
                print 'Dealer got BLACKJACK!'
                active = False
            elif sum(dealers_cards) > 21:
                print 'Dealer BUSTS! with {}'.format(dealers_cards)
                dealers_cards.append(0)
                active = False

def compare(players_cards, dealers_cards):
    for i in range(len(players_cards)):
        if sum(players_cards[i]) <= 21 and sum(dealers_cards) <= 21:
            if sum(players_cards[i]) < sum(dealers_cards):
                print 'Dealer beat Player {}. Dealer had {}, a total of {}; and Player had {}, a total of {}. Player loses his/her chips :('.format(i, dealers_cards, sum(dealers_cards), players_cards[i], sum(players_cards[i]))
            elif sum(dealers_cards) < sum(players_cards[i]):
                print 'Player {} beat the Dealer. Player had {}, a total of {}; and Dealer had {}, a total of {}. '.format(i, i, sum(players_cards[i]), dealers_cards, sum(dealers_cards))
            elif sum(players_cards[i]) == sum(dealers_cards):
                print 'Dealer and Player {} DRAW'.format(i)
            elif sum(players_cards[i]) == 21 and sum(dealers_cards) == 21:
                print 'Player {} and the Dealer both got BLACKJACK, so Player {} wins'.format(i, i)
        else:
            if 0 in players_cards[i]:
                print "Player {} BUSTS and lost their chips! :'(".format(i)
            elif sum(dealers_cards) > 21 and sum(players_cards[i]) <= 21:
                print 'Dealer BUSTS and Player {} did not BUST so Player {} automatically wins!'.format(i, i)




initial_deal_cards(num_players)
check_aces_players(players_cards)
hit_or_stick(players_cards)
check_aces_dealer(dealers_cards) #Check aces first because if dealer has between 17 and 21 there is no need to coninue
deal_dealer()
compare(players_cards, dealers_cards)
