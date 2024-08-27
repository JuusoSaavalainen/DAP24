#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    with open(filename) as f:
        l = []
        regex = r'(\d+) (\w{3})\s+(\d+)\s+(\d+):(\d+)\s+(.*)$'
        for line in f:
            found = re.findall(regex, line)
            for match in found:
                l.append(tuple(int(x) if x.isdigit() else x for x in match))
    return l


def main():
    print(file_listing())


if __name__ == "__main__":
    main()
