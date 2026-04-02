#!/usr/bin/python3
class Plant:
    name: str
    _height: float
    _age_old: int
    grow_day: float

    class _Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f"Stats: {self.grow_calls} grow"
                  f", {self.age_calls} age, {self.show_calls} show")

    def __init__(self, name: str, height: float, age_old: int) -> None:
        self.name = name
        self.height = height
        self.age_old = age_old
        self.grow_day = round(height / 31.25, 1)
        self.__stats = Plant._Stats()

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

    def grow(self, grow_day: float):
        self.height += grow_day
        self.__stats.grow_calls += 1

    def age(self, age: int) -> None:
        self.age_old += age
        self.__stats.age_calls += 1

    @classmethod
    def create_anonymus(cls):
        return cls("Unknow plant", 0, 0)

    @staticmethod
    def check_year(age: int) -> bool:
        return (age > 365)

    def show(self) -> None:
        self.__stats.show_calls += 1
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.age_old} days old")

    def display_stats(self):
        print(f"[statistics for {self.name.capitalize()}]")
        self.__stats.display()


class Flower(Plant):
    color: str
    blooming: bool

    def __init__(self,
                 name: str, height: float, age_old: int, color: str) -> None:
        self.color = color
        self.blooming = False
        super().__init__(name, height, age_old)

    def bloom(self) -> None:
        self.blooming = True
        print("[asking the rose to bloom]")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.blooming):
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    trunk_diameter: float
    shade: bool

    class _TreeStats(Plant._Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def display(self):
            super().display()
            print(f" {self.shade_calls} shade")

    def __init__(self,
                 name: str,
                 height: float, age_old: int, trunk_diameter: float) -> None:
        self.trunk_diameter = trunk_diameter
        self.shade = False
        super().__init__(name, height, age_old)
        self._stats = Tree._TreeStats()

    def produce_shade(self) -> None:
        self.shade = True
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self.height}"
              f"cm long and {self.trunk_diameter}cm wide.")
        self._stats.shade_calls += 1

    def show(self):
        self._stats.show_calls += 1
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display_stats(self):
        print(f"[statistics for {self.name}]")
        self._stats.display()


class Seed(Flower):
    seeds: int

    def __init__(self, name: str, height: float, age_old: int, color: str):
        self.seeds = 0
        super().__init__(name, height, age_old, color)

    def bloom(self):
        self.blooming = True
        self.seeds = 42

    def fast_grow(self, grow_day: float, age: int):
        print(f"[make {self.name} grow, age and bloom]")
        self.grow(grow_day)
        self.age(age)
        self.bloom()

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")


def main():
    f1 = Flower("rose", 15, 10, "red")
    t1 = Tree("Oak", 200.0, 365, 5.0)
    s1 = Seed("sunflower", 80.0, 45, "yellow")
    p1 = Plant.create_anonymus()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year(400)}")
    print()
    print("=== Flower")
    f1.show()
    f1.display_stats()
    f1.bloom()
    f1.grow(8)
    f1.show()
    f1.display_stats()
    print()
    print("=== Tree")
    t1.show()
    t1.display_stats()
    t1.produce_shade()
    t1.display_stats()
    print()
    print("=== Seed")
    s1.show()
    s1.fast_grow(30, 20)
    s1.show()
    s1.display_stats()
    print()
    print("=== Anonymous")
    p1.show()
    p1.display_stats()


if __name__ == "__main__":
    main()
