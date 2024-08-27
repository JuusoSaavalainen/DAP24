#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    print(triangle.hypotenuse(1, 2))
    print(triangle.area(2, 2))


if __name__ == "__main__":
    main()
