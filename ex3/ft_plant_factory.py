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
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.age_old} days old")
        

def main():
    p1 = Plant("rosa", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)
    plants = [p1, p2, p3, p4, p5]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
    

if __name__ == "__main__":
    main()
    