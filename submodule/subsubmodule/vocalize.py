import numpy as np
# requests:
import requests
# tqdm:
import tqdm


# types of line break:
_URL = ("http://svnweb.freebsd.org/csrg/share/dict/"
       "words?view=co&content-type=text/plain")

print("\n")
print("Caching words...", "\n")
# HTTP request:
words = []
# HTTP response:
response = requests.get(_URL, stream=True)
total_size = int(response.headers.get('content-length', 0))
block_size = 1024
for data in tqdm.tqdm(
        response.iter_content(block_size),
        total=np.ceil(total_size // block_size),
        unit='KB',
        unit_scale=True
    ):
    # list.extend:
    words.extend(data.splitlines())

# np.random:
# np.random.choice:
# str.decode:
# utf-8:
# void method:
def say_something() -> None:
    print(np.random.choice(words, 1)[0].decode("utf-8") + "!")
