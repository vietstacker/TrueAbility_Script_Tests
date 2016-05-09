#!/usr/bin/python

import optparse
import os
import sys

def check_ext(ext):
    if len(ext) == 4:
        if(len(ext.split('.')[1]) == 3):
            return True
    return False

def extension_extend(dir, ext):
    if check_ext(ext):
        for file in os.listdir(dir):
            abs_path = dir + "/" + file
            if not os.path.isdir(abs_path):
                new_path = ''.join([abs_path, ext])
                os.rename(abs_path, new_path)
    else:
        print("Invalid input. A three character extension is required.")
        sys.exit(19)


def main():
    parser = optparse.OptionParser()
    parser.add_option('-E', '--extension')

    options, args = parser.parse_args()
    extension = options.extension
    dir = "/var/dump/files"
    extension_extend(dir, extension)

if __name__ == "__main__":
    main()
