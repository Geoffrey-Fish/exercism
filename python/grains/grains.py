#SOLVED
def square(number):
    a = 0.5
    if number <= 0 or number  > 64 :
        raise ValueError("square must be between 1 and 64")
    if number == 1 :
        return 1
    for i in range(number) :
        a = a + a 
    return int(a)

def total():
    a = 1 
    for i in range(64) :
        a = a + a
        print(a)
    return a-1
print(total())
print(2**64)
