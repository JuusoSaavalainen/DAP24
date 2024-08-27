#!/usr/bin/env python3

def reverse_dictionary(d):
    rd = {}
    for key, val in d.items():
        for item in val:
            if item in rd:
                rd[item].append(key)
                continue
            rd[item] = [key]
    return rd


def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa',
                                         'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
