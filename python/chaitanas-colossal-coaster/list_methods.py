'''did I mention that I hate pylint? The care for things noobody needs,like, for real.'''
def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    '''adding it'''
    exp = express_queue
    norm = normal_queue
    if ticket_type == 1 :
        exp.append(person_name)
        return exp
    norm.append(person_name)
    return norm

def find_my_friend(queue, friend_name):
    '''why is here an unexpexted indent,dafuq???'''
    ende = queue
    here = ende.index(friend_name)
    return here

def add_me_with_my_friends(queue, index, person_name):
    '''Add me baby'''
    end = queue
    end.insert(index, person_name)
    return end

def remove_the_mean_person(queue, person_name):
    '''throw him out!'''
    out = queue
    out.remove(person_name)
    return out

def how_many_namefellows(queue, person_name):
    '''how many romans? ITE!'''
    count = queue.count(person_name)
    return count

def remove_the_last_person(queue):
    '''Sorry, we are closed'''
    name = queue[-1]
    return name

def sorted_names(queue):
    '''ABCDEFG'''
    abc = queue
    abc.sort()
    return abc
