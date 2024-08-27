#!/usr/bin/env python3

def word_frequencies(filename):
    dicti = {}
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word_strip = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word_strip in dicti:
                    dicti[word_strip] += 1
                    continue
                dicti[word_strip] = 1
    return dicti


def main():
    word_frequencies("src/alice.txt")


if __name__ == "__main__":
    main()
