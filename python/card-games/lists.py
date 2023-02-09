'''Time for some gambling!'''
def get_rounds(number):
    '''See if it works'''
    i = number[0]
    return list(number,i+1,i+2)

def concatenate_rounds(rounds_1, rounds_2):
   '''Internet, oh dear friend'''
   return rounds_1.extend(rounds_2)

def list_contains_round(rounds, number):
    '''True or what?'''
    return bool(number in rounds)

def card_average(hand):
    '''I know that one'''
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    '''not sure if this will work'''
	mid = (len(hand)/2)+1
	cut =(hand[0]+hand[mid]+hand[-1])/3
	return cut

def average_even_is_average_odd(hand):
	'''Lets try that'''
	even = []
	odd = []
	for i in range (len(hand)):
		if i % 2 == 0 :
			even.append(hand[i])
		else :
			odd.append(hand[i])
	even_av = sum(even)/len(even)
	odd_av = sum(odd)/len(odd)
	return bool(even_av == odd_av)

def maybe_double_last(hand):
    '''Easypeasy'''
    handi = hand
    if handi[-1] == 11 :
		handi[-1] = 22
		return handi
		
