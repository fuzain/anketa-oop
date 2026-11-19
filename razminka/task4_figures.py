# Задание 4. Фигуры и наследование
import math


class Figure:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def __str__(self):
        return f"{self.name}: площадь {self.area():.2f}"


class Rect(Figure):
    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    figures = [Rect(3, 4), Circle(2), Rect(5, 3)]
    total = 0
    for fig in figures:
        print(fig)
        total += fig.area()
    print()
    print(f"Общая площадь: {total:.2f}")
