#!/usr/bin/python3
class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm {self.age} days old")


def main():
    p1 = Plant("rose", 25, 30)
    p2 = Plant("sunflowe", 80, 45)
    p3 = Plant("cactus", 15, 120)
    p1.show()
    p2.show()
    p3.show()


if __name__ == "__main__":
    main()
