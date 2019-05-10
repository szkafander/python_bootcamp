# relative import:
from .subsubmodule import vocalize

# what happens when a module is loaded?:
print("Saying a word...", "\n")
# module member:
vocalize.say_something()
