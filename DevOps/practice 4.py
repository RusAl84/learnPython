import os
from datetime import datetime
import hashlib

def print_details(a):
    print(f"{a=}\ta.id: {id(a)}\ntype of a:{type(a)}\nis a an object:{isinstance(a, object)}\n")

if __name__ == "__main__":
    # Everything is an Object, one more time with feeling
    print_details(a=1)
    print_details(a="Hello world!")
    print_details(a=datetime.now())
    print_details(a=os.path.realpath("./"))
