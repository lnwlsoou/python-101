"""
    xxx
"""
import value_operations
# from value_operations import swap
from fizz_buzz import fizzbuzz

print(__name__)
if __name__ == "__main__":
    NUMBER = 3
    print(NUMBER)

    NAME = "sopa"
    print(NAME)

    if NUMBER == 3:
        print("Number is 3")
        print("Inside IF")
    print("Outside IF")

    fruits = ["Orange", "Apple", "Durian"] # iterable
    print(fruits[0])

    # for i in range(0, len(fruits)):
    #     print(i, fruits[i])
    for i, fruit in enumerate(fruits):
        print(i, fruit)

    company = ("Github", "SF, USA") # this variable cannot change value
    company_name, location = company
    print(company_name, location)

    A = 5
    B = 10
    B, A = A, B
    print(A, B)
    print(value_operations.swap(1, 2))

    for number in range(16):
        print(fizzbuzz(number))
