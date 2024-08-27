#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(image: np.ndarray) -> np.ndarray:
    weights = np.array([0.2126, 0.7152, 0.0722])
    grayscale_image = np.dot(image[..., :3], weights)
    return grayscale_image


def to_red(image: np.ndarray) -> np.ndarray:
    red_image = np.copy(image)
    red_image[..., [1, 2]] = 0
    return red_image


def to_green(image: np.ndarray) -> np.ndarray:
    green_image = np.copy(image)
    green_image[..., [0, 2]] = 0
    return green_image


def to_blue(image: np.ndarray) -> np.ndarray:
    blue_image = np.copy(image)
    blue_image[..., [0, 1]] = 0
    return blue_image


def main():
    # img source
    img = plt.imread("src/painting.png")

    # 1)
    grey_img = to_grayscale(img)
    plt.imshow(grey_img)
    plt.gray()

    # 2)
    red_img = to_red(img)
    green_img = to_green(img)
    blue_img = to_blue(img)

    # plotting
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(red_img)
    ax[1].imshow(green_img)
    ax[2].imshow(blue_img)
    plt.show()


if __name__ == "__main__":
    main()
