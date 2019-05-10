import numpy as np
import requests

_URL = ("http://svnweb.freebsd.org/csrg/share/dict/"
       "words?view=co&content-type=text/plain")

print("\n")
print("Caching words...", "\n")
# HTTP request:
words = requests.get(_URL).content.splitlines()

# np.random:
# np.random.choice:
# str.decode:
# utf-8:
def say_something() -> None:
    print(np.random.choice(words, 1)[0].decode("utf-8") + "!")
