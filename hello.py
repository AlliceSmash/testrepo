import math
import sys
from os import rename

import requests


# print(sys.version)
print(sys.executable)
def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting


# print(greet('world'))
# print(greet('Mark'))
# r = requests.get("http://spiezio.net")
# print(r.status_code)

name = input("your name?")
print("hello, ", name)