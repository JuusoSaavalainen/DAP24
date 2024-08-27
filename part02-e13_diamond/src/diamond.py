#!/usr/bin/env python3

import numpy as np


def diamond(n):
    identity = np.eye(n, dtype=int)
    mirror_identity = np.flip(identity, axis=1)
    top = np.concatenate((mirror_identity, identity[:, 1:]), axis=1)
    bottom = np.concatenate((identity, mirror_identity[:, 1:]), axis=1)
    return np.concatenate((top, bottom[1:, :]), axis=0)


def main():
    print(diamond(1))


if __name__ == "__main__":
    main()
