#!/usr/bin/python3
class Plant:
    name: str
    _height: float
    _age_old: int
    grow_day: float

    def __init__(self, name: str, height: float, age_old: int) -> None:
        self.name = name
        self.height = height
        self.age_old = age_old
        self.grow_day = round(height / 31.25, 1)

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = height
            print(f"Height updated: {height}cm")

    def get_height(self) -> float:
        return (self.height)

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.age_old = age
            print(f"Age update: {age} days")

    def get_age(self) -> int:
        return (self.age_old)

    def grow(self) -> None:
        self.height = self.height + self.grow_day

    def age(self) -> None:
        self.age_old += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.age_old} days old")


def main():
    p1 = Plant("rose", 15, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    p1.show()
    print("")
    p1.set_height(25)
    p1.set_age(30)
    print("")
    p1.set_height(-1)
    p1.set_age(-1)
    print("")
    print("Current state: ", end="")
    p1.show()


if __name__ == "__main__":
    main()
