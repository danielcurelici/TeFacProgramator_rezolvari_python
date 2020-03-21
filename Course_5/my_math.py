from math import sqrt

global total, primes, squares
total = primes = squares = 0

def check_prime(x):
    """
    This function checks if an integer is a prime number and increases the
    primes global variable accordingly
    Parameters:
        -x  :   number  => the number to be checked
    """
    global primes
    if x <= 1:
        return
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return
    primes += 1
    
def check_perfect_square(x):
    """
    This function checks if an integer is a perfect square and increases the
    squares global variable accordingly
    Parameters:
        -x  :   number  => the number to be checked
    """
    global squares
    if x == int(sqrt(x)) ** 2:  #a better condition is x == int(sqrt(x) + 0.5) ** 2
        squares += 1
    
if __name__ == "__main__":
    print("Press q to quit")
    while True:
        x = input("x=")
        if x == "q":
            break
        if x.isdigit():
            check_prime(int(x))
            check_perfect_square(int(x))
            total += 1
            print("primes: %i\nsquares: %i\ntotal_checked: %i" % \
            (primes, squares, total))
        else:
            print("Wrong input. Insert an integer or the letter \"q\"")
            