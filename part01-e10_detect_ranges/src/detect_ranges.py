#!/usr/bin/env python3

def detect_ranges(L):
    A = sorted(L)
    helpls = []
    res = []
    for i in A:

        if helpls == []:
            helpls.append(i)
            continue

        if i - helpls[-1] == 1:
            helpls.append(i)
            if i == A[-1]:
                res.append((helpls[0], helpls[-1]+1))
            continue

        else:
            if len(helpls) > 1:
                res.append((helpls[0], helpls[-1]+1))
                helpls = [i]
                if i == A[-1]:
                    res.append(i)
                continue

            res.append(helpls[-1])
            helpls = [i]

            if i == A[-1]:
                res.append(i)
    return res


def main():
    L = [1, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
