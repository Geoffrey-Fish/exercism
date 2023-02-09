one = (1, 2)
print(type(one))
t00ple = (1, 2)
print(bool(type(t00ple) == tuple))


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


print(higher_card("6", "K"))
