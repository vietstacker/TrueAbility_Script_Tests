#!/usr/bin/python

import string
import random

def id_generator(size=9, chars=string.ascii_letters + string.digits):
    result = ''.join(random.choice(chars) for _ in range(size))
    if any(char.isdigit() for char in result):
        return result

def main():
    id_generator()

if __name__ == "__main__":
    main()
