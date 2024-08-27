#!/usr/bin/env python3

import math


def main():
    valid_shapes = ["circle", "rectangle", "triangle"]
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")

        if shape == "":
            break

        if shape not in valid_shapes:
            print("Unknown shape!")
            continue

        if shape == "circle":
            rad = float(input("Give radius of the circle: "))
            print(f"The area is {rad * rad * math.pi}")
            continue

        if shape == "rectangle":
            length = float(input("Give width of the rectangle: "))
            width = float(input("Give height of the rectangle: "))
            print(f"The area is {length * width}")
            continue

        if shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            print(f"The area is {base * height / 2}")
            continue


if __name__ == "__main__":
    main()
