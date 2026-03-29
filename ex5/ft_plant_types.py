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

    def grow(self, grow_day: float):
        self.height += grow_day

    def age(self, age: int) -> None:
        self.age_old += age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.age_old} days old")


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

    def __init__(self,
                 name: str,
                 height: float, age_old: int, trunk_diameter: float) -> None:
        self.trunk_diameter = trunk_diameter
        self.shade = False
        super().__init__(name, height, age_old)

    def produce_shade(self) -> None:
        self.shade = True
        print("[asking the oak to produce shade]")

    def show(self):
        if (self.shade):
            print(f"Tree {self.name.capitalize()} now produces a shade of "
                  f"{self.height:.1f}cm long and "
                  f"{self.trunk_diameter:.1f}cm wide.")
        else:
            super().show()
            print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: int

    def __init__(self, name: str, height: float,
                 age_old: int, harvest_season: str) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        super().__init__(name, height, age_old)

    def age(self, age: int) -> None:
        self.age_old += age
        self.grow(age * 2.1)
        self.nutritional_value += age
        print(f"[make tomato grow and age for {self.age_old} days]")

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main():
    f1 = Flower("rose", 15, 10, "red")
    t1 = Tree("oak", 200, 365, 5)
    v1 = Vegetable("tomato", 5, 10, "April")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    f1.show()
    f1.bloom()
    f1.show()
    print("")
    print("=== Tree")
    t1.show()
    t1.produce_shade()
    t1.show()
    print("")
    print("=== Vegetable")
    v1.show()
    v1.age(20)
    v1.show()


if __name__ == "__main__":
    main()
