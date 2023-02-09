#SOLVED
'''This is the prettified version'''
def eat_ghost(power_pellet_active, touching_ghost):
    '''lets look at this bool// Oh nose, there is a trailing whitespace in line 5,boohoo...'''
    return bool( power_pellet_active is True and touching_ghost is True)

def score(touching_power_pellet, touching_dot):
    '''Antoher bool'''
    return bool(touching_power_pellet is True or touching_dot is True)

def lose(power_pellet_active, touching_ghost):
    '''The las bool ?'''
    return bool(power_pellet_active is False and touching_ghost is True)

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    '''Missing final line after code, my good lord!!!'''
    return bool(has_eaten_all_dots is True and lose(power_pellet_active,touching_ghost) is False)
