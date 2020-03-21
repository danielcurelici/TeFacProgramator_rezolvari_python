#we import the modules we created
import my_math
import my_string

if __name__ == "__main__":
    #we generate a list of numbers from 0 to 9 and test the functions from
    #the my_math module and print the global variables updated in them
    numbers = list(range(10))
    print(numbers)
    for num in numbers:
        my_math.check_prime(num)
        my_math.check_perfect_square(num)
        print("We checked the number: " + str(num))
        print("Primes so far: " + str(my_math.primes))
        print("Perfect squares so far: " + str(my_math.squares))
        print()
        
    #we initialize our string with some nice quotes from Jericho Swain.
    text = "i was born a patrician. i became a soldier. the mud on our boots \
will hide the bloodstains. destiny marches, like any man."
    #we call the functions from my_string module and print the results
    print(my_string.capitalize_sentence(text))
    print(my_string.letter_count_dict_long(text))