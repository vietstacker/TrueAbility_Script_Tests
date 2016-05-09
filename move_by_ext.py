#!/usr/bin/python

import os

def dir_existence(dir):
    try:
        os.makedirs(dir)
    except OSError:
        if os.path.isdir(dir):
            pass
            

def file_moving(dir, dest1, dest2, dest3):
    for file in os.listdir(dir):
        abs_path = dir + "/" + file
        if not os.path.isdir(abs_path):
            if file.split('.')[1] == "mov":
                os.system("mv " + abs_path + " " + dest1)
            elif file.split('.')[1] == "jpg":
                os.system("mv " + abs_path + " " + dest2)
            elif file.split('.')[1] == "doc":
                os.system("mv " + abs_path + " " + dest3)
            else:
                os.system("rm" + " " + abs_path)


def main():
    dir = "/data/downloads/incoming/"
    dest1 = "/data/downloads/movies"
    dest2 = "/data/downloads/images"
    dest3 = "/data/downloads/docs"
    dir_existence(dest1)
    dir_existence(dest2)
    dir_existence(dest3)
    file_moving(dir, dest1, dest2, dest3)

if __name__ == "__main__":
    main()
