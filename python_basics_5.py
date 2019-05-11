
#%%
import functools
import itertools
from typing import List


lambda_method = lambda x: print("A lambda method with argument: {}".format(x))

print("\n")
lambda_method("yoyoyo")

# recursion:
# factorial:
def factorial(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

# lambda arithmetic:
# Y combinator:
# functional programming:
Y = lambda f: lambda *args: f(Y(f))(*args)
factorial_lambda = lambda f: lambda n: (1 if n < 2 else n * f(n - 1))

print("\n")
print("Factorial of 5: {}".format(factorial(5)))
print("Factorial of 5 with lambda expr.: {}".format(Y(factorial_lambda)(5)))

#%% filtering iterables

# filtering:
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# filtered list comprehension:
def is_odd(number: int) -> bool:
    if number%2 == 0:
        return False
    return True

filtered_list = [element for element in some_list if is_odd(element)]

print("\n")
print("some_list: {}".format(some_list))
print("Odd numbers in some_list: {}".format(filtered_list))

filtered_list_w_filter = filter(is_odd, some_list)

print("\n")
print("A filtered object is type: {}".format(type(filtered_list_w_filter)))
print("\n")
print("Odd numbers with filter: {}".format(list(filtered_list_w_filter)))

#%% reducing iterables

# reducing:
def sum_list(a_list: List[int]) -> int:
    sum_ = 0
    for element in a_list:
        sum_ += element
    return sum_

print("\n")
print("The sum of some_list: {}".format(sum_list(some_list)))

summed_w_reduce = functools.reduce(lambda x, y: x + y, some_list)

print("\n")
print("The sum of some_list with reduce: {}".format(summed_w_reduce))

#%% mapping iterables

# mapping:
mapped_list = [element*2 for element in some_list]
mapped_list_w_map = map(lambda x: x*2, some_list)

print("\n")
print("Map objects are type {}".format(type(mapped_list_w_map)))

print("\n")
print("Mapped list: {}".format(mapped_list))
print("Mapped list with map: {}".format(list(mapped_list_w_map)))

#%% combinatorics

short_list = [1, 2, 3, 4]
short_str_list = ["a", "b", "c", "d"]

# permutation:
permutations = itertools.permutations(short_list, 2)

# combination:
combinations = itertools.combinations(short_list, 3)

print("\n")
print("Short list: {}".format(short_list))
print("Permutations of short list, groups of 2: {}".format(list(permutations)))
print("Combinations of short list, groups of 3: {}".format(list(combinations)))

#%%

generator_numbers = (element for element in short_list)
generator_names = (element for element in short_str_list)

# endless cycling, no generator exhaustion
for k, element in enumerate(itertools.cycle(generator_numbers)):
    print(element)
    if k > 30:
        print("This would go on forever, breaking...")
        break
    
#%%
# why do we redefine these generators?:
generator_numbers = (element for element in short_list)
generator_names = (element for element in short_str_list)    
    
# cartesian product:
for k, element in enumerate(itertools.cycle(
        itertools.product(generator_numbers, generator_names))):
    print(element)
    if k > 30:
        print("This would go on forever, breaking...")
        break


# from itertools
# chain:
# compress:
# groupby:
# starmap:
# tee:

#%%

generator_numbers = (element for element in short_list)
generator_names = (element for element in short_str_list)

# zip:
for vals in zip(generator_numbers, generator_names):
    print(vals)

#%%
    
# list unpacking:
def method(*args) -> None:
    for k, arg in enumerate(args):
        print("Value of the {}th argument is {}".format(k, arg))

print("\n")
print("We call a method with a variable number of arguments...")
method(1, 2, 3, 4, 5)

#%%

# dict unpacking:
def method(*args, **kwargs) -> None:
    for k, arg in enumerate(args):
        print("Value of the {}th argument is {}".format(k, arg))
    for key, val in kwargs.items():
        print("Value of the keyword argument {} is {}".format(key, val))
        
print("\n")
print("We call a method with a variable number of arguments...")
method(1, 2, 3, vaj=5, tej=2, kifli=3)
