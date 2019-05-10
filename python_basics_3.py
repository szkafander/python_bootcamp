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

from typing import Callable

#%% classes miscellanea

# operator overloading:
class OverloadedMetric:
    
    # explain what this class does and how it works:
    
    # private attribute:
    # class attribute:
    _accepted_units = ("m", "cm", "mm")
    
    # __init__:
    # None:
    def __init__(self, value: float, unit: str = "m") -> None:
        # private instance attribute:
        self._value = value * self._conversion_factor(unit)
        self._unit = unit
        
    # private static method:
    # ValueError:
    # in:
    @staticmethod
    def _check_unit(new_unit: str) -> None:
        if new_unit not in OverloadedMetric._accepted_units:
            raise ValueError("{} not in accepted units.".format(new_unit))
    
    # private class method:
    def _conversion_factor(self, new_unit: str) -> int:
        self._check_unit(new_unit)
        if new_unit == "m":
            return 1
        elif new_unit == "cm":
            return 0.01
        elif new_unit == "mm":
            return 0.001
    
    # property:
    @property
    def unit(self):
        return self._unit
    
    # setter:
    @unit.setter
    def unit(self, new_unit: str):
        self._check_unit(new_unit)
        self._unit = new_unit
    
    @property
    def value(self):
        return self._value / self._conversion_factor(self.unit)
    
    @value.setter
    def value(self, new_value: float):
        self._value = new_value
    
    # __str__:
    def __str__(self) -> str:
        return "{} {}".format(round(self.value, 3), self.unit)
    
    # __repr__:
    def __repr__(self) -> str:
        return str(self)
    
    # __add__:
    # forward-referencing type hint:
    def __add__(self, other: "OverloadedMetric") -> "OverloadedMetric":
        return OverloadedMetric(
                ((self._value + other._value) 
                 / self._conversion_factor(self.unit)),
                unit = self.unit
            )
    
    # __gt__, __lt__, __ge__, __le__:
    def __gt__(self, other: "OverloadedMetric") -> bool:
        return self._value > other._value
    
    def __lt__(self, other: "OverloadedMetric") -> bool:
        return self._value < other._value
    
    def __ge__(self, other: "OverloadedMetric") -> bool:
        return self._value >= other._value
    
    def __le__(self, other: "OverloadedMetric") -> bool:
        return self._value <= other._value
    
    # chainable pattern:
    def to_unit(self, new_unit: str) -> "OverloadedMetric":
        self._check_unit(new_unit)
        return OverloadedMetric(
                self._value / self._conversion_factor(new_unit),
                unit = new_unit
            )


five_mm = OverloadedMetric(5, "mm")
eleven_cm = OverloadedMetric(11, "cm")
two_m = OverloadedMetric(2, "m")

sum_length = five_mm + eleven_cm + two_m

print("\n")
print("2 m + 11 cm + 5 mm = {}".format(sum_length.to_unit("cm")), "\n")

sum_length.unit = "mm"
print("set sum unit to mm. sum_length: {}".format(sum_length), "\n")

# try:
# except:
# ...Error as:
print("trying to set sum unit to km...")
try:
    # which method is called here?:
    sum_length.unit = "km"
except ValueError as error:
    print(("can't do that, km is not accepted. "
           "original error message: {}".format(str(error))))

print("\n")
print("is five millimeters longer than two meters?: {}".format(
        five_mm > two_m))
print("is eleven centimeters longer than five millimeters?: {}".format(
        eleven_cm > five_mm))


#%% a parameterizable decorator

# decorator:
# decorator method:
def decorator_with_parameter(decorator_parameter: str) -> Callable:
    
    def decorator(method: Callable) -> Callable:
        
        # list unpacking:
        # dict unpacking:
        # positional argument:
        # keyword argument:
        def wrapper(*args, **kwargs) -> None:
            print("\n")
            print("This is a decorator that says: {}".format(
                    decorator_parameter))
            method(*args, **kwargs)
        
        return wrapper
    
    return decorator


@decorator_with_parameter("Hi!")
def method_to_decorate(argument):
    print("My argument is: {}".format(argument))


method_to_decorate("Ho!")


class DecoratorWithParameter:
    
    # __init__:
    def __init__(self, decorator_parameter: str) -> None:
        self.decorator_parameter = decorator_parameter
    
    # __call__:
    def __call__(self, method: Callable) -> Callable:
        
        def wrapper(*args, **kwargs) -> None:
            print("\n")
            print("This is a class decorator that says: {}".format(
                    self.decorator_parameter))
            method(*args, **kwargs)
        
        return wrapper


# class instantiation:
parameterized_decorator = DecoratorWithParameter("Yo!")


@parameterized_decorator
def another_method_to_decorate(argument):
    print("And my argument is: {}".format(argument))


@parameterized_decorator
def yet_another_method_to_decorate(argument):
    print("Here's another: {}".format(argument))
    
    
another_method_to_decorate("Ho!")
yet_another_method_to_decorate("Ha!")
