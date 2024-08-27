#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    centr_x = (a.shape[1] - 1) / 2
    centr_y = (a.shape[0] - 1) / 2
    return (centr_y, centr_x)   # note the order: (center_y, center_x)


def radial_distance(a):
    c_point = center(a)
    i, j = np.indices(a.shape[:-1], sparse=True)
    return np.sqrt((i-c_point[0])**2 + (j-c_point[1])**2)


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    a_min = np.min(a)
    a_max = np.max(a)
    return tmin + (a - a_min) * (tmax - tmin) / (a_max - a_min)


def radial_mask(a):
    dist = radial_distance(a)
    if dist.shape[0] <= 2 or dist.shape[1] <= 2:
        return np.ones(dist.shape)
    mask = scale(dist)
    return 1 - mask


def radial_fade(a):
    mask = np.expand_dims(radial_mask(a), axis=-1)
    return a * mask


def main():
    img = plt.imread("src/painting.png")

    radial_mask_pic = radial_mask(img)
    radial_fade_pic = radial_fade(img)

    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(img)
    ax[1].imshow(radial_mask_pic)
    ax[2].imshow(radial_fade_pic)
    plt.show()

    radial_2 = radial_mask(np.array([[[1], [1]]]))
    print(radial_2.shape)


if __name__ == "__main__":
    main()
