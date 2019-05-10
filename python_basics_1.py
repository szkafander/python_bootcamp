# python alapok

# Python telepítése (Windows rendszeren):
# 1. Anaconda letöltése és telepítése: 
#     https://www.anaconda.com/distribution/#download-section
# 2. Spyder IDE elindítása
# 3. Megnyitni ezt a fájlt Spyder-ben
# 4. A fájl cellákból áll. Egy cella két '#%%' közötti szövegrész. Ha a kurzor
#     egy adott cellában villog, akkor azt a cellát a Ctrl+Enter billentryű
#     kombinációval tudjátok futtatni.
# 5. A cellákat egymás után, fentről lefelé haladva érdemes futtatni.

# feladat 1: ahol láttok egy kifejezést egy kettősponttal, oda a kettőspont 
# után írjátok le hogy mit jelent az adott kifejezés, mire jó, és hogyan kell 
# használni. lehetőleg angol nyelven írjatok.
#
# pl.:
#
# import: betölt egy modult, aminek változóit, metódusait és osztályait az
# importálás után használhatjuk. az importálandó modulnak a Python path-en
# megtalálhatónak kell lennie.
#
# feladat 2: minden részt és minden részletet értsetek meg ebből a fájlból.
#
# a feladat innentől angolul van. ezt azért jó megszokni, mert minden 
# internetes forrás is angolul lesz.

#%%
# # (comment):
# """ ... """ (block comment):
# import:
# import ... as:
# collections:
import collections as coll

# from:
# from ... import:
# typing:
# Callable, Optional, Tuple: ... írj még példákat
from typing import Callable, Iterable, Optional, Tuple

#%%
# = (assignment) operator:
# float:
a_float = 1.5
another_float = 2.3

# print:
# type:
# string formatting:
print("type of a float: {}".format(type(a_float)))
print("type of another float: {}".format(type(another_float)))

#%%
# int:
an_int = 1
another_int = -2

# + operator:
# - operator:
# * operator:
# / operator:
# // operator:
# % operator:
# <, > operators:
# <=, >= operators:
# == operator:
# escape characters:
# \n:
print("\n")
print("an_int + another_int: {}".format(an_int + another_int))
print("an_int - another_int: {}".format(an_int - another_int))
print("an_int * another_int: {}".format(an_int * another_int))
print("an_int / another_int: {}".format(an_int / another_int))
print("an_int // another_int: {}".format(an_int // another_int))
print("an_int % another_int: {}".format(an_int % another_int))
print("an_int > another_int: {}".format(an_int > another_int))
print("an_int < another_int: {}".format(an_int < another_int))
print("an_int <= another_int: {}".format(an_int <= another_int))
print("an_int >= another_int: {}".format(an_int >= another_int))
print("an_int == another_int: {}".format(an_int == another_int))

# bool:
a_bool = True
another_bool = False

# and:
# or:
# not:
print("\n")
print("a_bool: {}".format(a_bool))
print("another_bool: {}".format(another_bool))
print("not a_bool: {}".format(not a_bool))
print("a_bool and another_bool: {}".format(a_bool and another_bool))
print("a_bool or another_bool: {}".format(a_bool or another_bool))

# string:
a_string = "aaa"
another_string = "bbc"

#%%
# list:
some_list = [a_string, "bla_bla_bla", 5, an_int, a_float, another_string]

# list indexing:
print("\n")
print("first element of list: {}".format(some_list[0]))
print("second element_of_list: {}".format(some_list[1]))
print("last element of list: {}".format(some_list[-1]))

#%%

print("\n")
print("original list: {}".format(some_list))

# list append:
some_list.append("new string")

print("list after append: {}".format(some_list))

# list pop:
some_list.pop(2)
print("list after append and pop(2): {}".format(some_list))

# list reverse:
print("reversed list: {}".format(list(reversed(some_list))))

#%%
# tuple
some_tuple = (an_int, a_float, another_string)

# can we append to a tuple?:

# dict
some_dict = {
        "a_field": 2,
        "another_field": 3.412,
        a_string: a_bool,
        another_string: some_list
    }

print("\n")
print("value of field '{}' of the dict: {}".format(
        a_string, some_dict[a_string]))
print("value of field '{}' of the dict: {}".format(
        another_string, some_dict[another_string]), "\n")

# OrderedDict:
# coll:
ordered_dict = coll.OrderedDict(some_dict)

#%%
# set:
a_set = {1, 2, 3, 4, 5, 5, 5, 6, 1, 1}
another_set = {4, 7, 3, 5}

print("\n")
print("a set: {}".format(a_set))
print("another set: {}".format(another_set))
print("the union of the two sets: {}".format(a_set.union(another_set)))
print("intersection of the two sets: {}".format(
        a_set.intersection(another_set)), "\n")

#%%
# iteration:
# for loop:
print("\n")
print("iteration...")
for element in some_list:
    print(element)
    
# enumerate:
print("\n")
print("enumeration...")
for index, element in enumerate(some_list):
    print("the {}th element is: {}".format(index, element))
    
# while loop:
# len:
# += operator:
print("\n")
print("while loop...")
k = 0
while k < len(some_list):
    print(some_list[k])
    k += 1

#%%
# list comprehension:
comprehended_list = [2*a for a in [1,2,3,4]]

print("\n")
print("comprehended list: {}".format(comprehended_list))
