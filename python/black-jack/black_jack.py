"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
#should I put some global definitions inside here?

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, 'A' = 1) numerical value otherwise.
    """
    if card == "J" or card == "Q" or card == "K":
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 1, all others are numerical value.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    if one > two:
        return str(one)
    if one < two:
        return str(two)
    if one == two:
        return tuple(one, two)

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card (J, Q, K == 10, numerical value otherwise)
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    three = one + two
    if (three + 11) > 21:
        return 1
    else:
        return 11

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 11, all others are numerical value.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    if one == 1:
        one = 11
    if two == 1:
        two = 11
    three = one + two
    return bool(three == 21)

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    t00ple = higher_card(card_one, card_two)
    return bool(type(t00ple) == tuple)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    three = one + two
    if three == 9 or three == 10 or three == 11:
        return True
    else:
        return False
