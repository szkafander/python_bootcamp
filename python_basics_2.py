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
# miért működik ez a script úgy, ahogy?
#
# a feladat innen angolul van. ezt azért jó megszokni, mert minden 
# internetes forrás is angolul lesz.

from typing import Callable, Iterable, Tuple

#%%
# methods:
# def:
def some_method(
        argument_1: int,
        argument_2: float,
        keyword_argument_1: str = "something",
        keyword_argument_2: int = 0
    ) -> Tuple[int, float, str, float]:
    return_var_1 = argument_1 * 2
    return_var_2 = argument_2 * 1.231
    return_var_3 = keyword_argument_1 + ", but what?"
    return_var_4 = keyword_argument_2 / 1.783
    return (
            return_var_1,
            return_var_2,
            return_var_3,
            return_var_4
        )

print("\n")
print("output of some_method(3, 1.571, keyword_argument_1='wait'): {}".format(
        some_method(3, 1.571, keyword_argument_1="wait")))

#%%
# a nested method
def nested_method(
        argument_1: float,
        argument_2: float
    ) -> Callable:
    
    def inner_method(argument: float) -> float:
        return argument * argument_1 + argument_2
    
    return inner_method

parametrized_method = nested_method(2.1, 1.4)

print("\n")
print("parametrized method is type {}".format(type(parametrized_method)))
print("output of parametrized method is type {}".format(
        type(parametrized_method(5))))

#%%
# class:
class SomeClass:
    
    # methods with double underscore names '__...__':
    # __init__:
    # self:
    def __init__(
            self, 
            attribute_1: str, 
            attribute_2: str
        ) -> None:
        self.attr_1 = attribute_1
        self.attr_2 = attribute_2
        
    # __str__:
    def __str__(self) -> str:
        return ("this is a class with two attributes. "
                "they have values '{}' and '{}'.".format(
                        self.attr_1, self.attr_2))
    
    # __repr__:
    def __repr__(self) -> str:
        return str(self)
    
    # __call__:
    def __call__(self, another: str) -> str:
        # string concatenation:
        return self.attr_1 + "_" + self.attr_2 + "_" + another
    
    # class methods:
    def class_method(self, separator: str) -> str:
        return separator.join((self.attr_1, self.attr_2))
    
    # @:
    # decorator:
    # staticmethod:
    @staticmethod
    def static_method(add_this: int, to_this: int) -> int:
        return add_this + to_this


# class instantiation:
class_instance = SomeClass("first attribute", "second attribute")

print("\n")
print("we instantiated a class.", class_instance, "\n")

print("the output of the class method: {}".format(
        class_instance.class_method(" ~ ~ ~ ")), "\n")

print("the output of the static method: {}".format(
        SomeClass.static_method(3, 5)), "\n")

#%%
# lazy evaluation:
# generators:
# generator comprehension:
comprehended_generator = (a for a in [0, 1, 2, 3, 4])

print("\n")
print("the generator: {}".format(comprehended_generator))

print("iterating over the comprehended generator:")
for element in comprehended_generator:
    print(element)

print("\n")
print("generator exhausted.")
for element in comprehended_generator:
    print(element)
print("no more elements are printed.")

# yield:
def generator_method(num_yields: int):
    k = 0
    while k < num_yields:
        yield k
        k += 1

generator = generator_method(5)

print("\n")
print("iterating over generator method:")
for element in generator:
    print(element)


class GeneratorClass:
    
    def __init__(self, num_yield: int) -> None:
        self.num_yield = num_yield
        self.counter = - 1
    
    # __iter__:
    def __iter__(self) -> Iterable:
        return self
    
    # __next__:
    # raise:
    # statement:
    # StopIteration:
    def __next__(self) -> int:
        if not self.counter < self.num_yield - 1:
            raise StopIteration
        self.counter += 1
        return self.counter

generator = GeneratorClass(5)

print("\n")
print("iterating over generator class:")
for element in generator:
    print(element)
