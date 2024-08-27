#!/usr/bin/env python3

def extract_numbers(s):
    listaus = []
    for element in s.split():
        try:
            listaus.append(int(element))
        except Exception:
            try:
                listaus.append(float(element))
            except Exception:
                continue
    return listaus


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
