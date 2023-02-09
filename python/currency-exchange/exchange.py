'''For fucks sake, he whines because there is no module docsting.dafuq'''
def exchange_money(budget, exchange_rate):
    '''the simple calculation of the amount you would get without a fee.'''
    return budget/exchange_rate


def get_change(budget, exchanging_value):
    '''the rest of your money after changing'''
    return budget-exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    '''How much the money is worth'''
    return int(denomination*number_of_bills)


def get_number_of_bills(budget, denomination):
    '''How many bills you get'''
    return int(budget//denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    '''the amount of money you can change'''
    spre = spread/100
    cost = exchange_rate*spre
    fee = exchange_rate+cost
    change = budget/fee
    bills = change//denomination
    amount = bills * denomination
    return int(amount)


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    '''the rest that you can not change'''
    spre = spread/100
    cost = exchange_rate*spre
    fee = exchange_rate+cost
    change = budget/fee
    bills = change//denomination
    b_worth = bills*denomination
    return int(change - b_worth)
