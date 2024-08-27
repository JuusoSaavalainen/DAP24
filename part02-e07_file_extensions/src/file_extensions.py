#!/usr/bin/env python3

def file_extensions(filename):
    dicti = {}
    listi = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if "." not in line:
                listi.append(line)
                continue
            else:
                elem_key = line.split(".")[-1]
                if elem_key in dicti.keys():
                    dicti[elem_key] += [line]
                    continue
                dicti[elem_key] = [line]
    return (listi, dicti)


def main():
    data = file_extensions("src/filenames.txt")
    print(f'{len(data[0])} files with no extension')
    dicti = data[1]
    for i in sorted(dicti.keys()):
        print(f'{i} {len(dicti[i])}')


if __name__ == "__main__":
    main()
