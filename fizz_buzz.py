'''
FizzBuzz
'''
def is_longtual(number, divider):
    ''' checking '''
    return number % divider == 0


def fizzbuzz(number):
    ''' fizzbuzz '''

    is_fizz = is_longtual(number, 3)
    is_buzz = is_longtual(number, 5)

    if is_fizz and is_buzz:
        result = "FizzBuzz"
    elif is_fizz:
        result = "Fizz"
    elif is_buzz:
        result = "Buzz"
    else:
        result = number

    if number == 0:
        result = number
    return result

if __name__ == "__main__":
    print(fizzbuzz(9))
    print(fizzbuzz(10))
    print(fizzbuzz(15))
    print(fizzbuzz(2))