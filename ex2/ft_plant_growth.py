#!/usr/bin/python3
class Plant:
    name: str
    height: float
    age_old: int
    grow_day: float

    def __init__(self, name: str, height: float, age_old: int) -> None:
        self.name = name
        self.height = height
        self.age_old = age_old
        self.grow_day = round(height / 31.25, 1)

    def grow(self) -> None:
        self.height = self.height + self.grow_day

    def age(self) -> None:
        self.age_old += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              "{self.age_old} days old")


def main():
    days = 7
    p1 = Plant("rose", 25, 30)
    for i in range(1, days + 1):
        print("=== Garden Plant Growth ===")
        print(f"=== Day {i} ===")
        p1.show()
        p1.grow()
        p1.age()
    print(f"Growth this week: {round(p1.grow_day * days)}cm")


if __name__ == "__main__":
    main()
