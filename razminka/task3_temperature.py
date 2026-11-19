# Задание 3. Класс Temperature


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def __str__(self):
        return f"{self.celsius:.1f} C = {self.fahrenheit:.1f} F"

    def __lt__(self, other):
        return self.celsius < other.celsius


if __name__ == "__main__":
    temps = [Temperature(21.5), Temperature(-3), Temperature(10)]
    print(temps[0])
    print(temps[1])
    print()
    print("по возрастанию:")
    for t in sorted(temps):
        print(t)
    print()
    print("самый тёплый:", max(temps))
