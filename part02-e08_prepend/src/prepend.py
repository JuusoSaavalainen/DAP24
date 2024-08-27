#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, preset):
        self.pre = preset

    def write(self, input):
        print(self.pre+input)


def main():
    p = Prepend("+++ ")
    p.write("Hello")


if __name__ == "__main__":
    main()
