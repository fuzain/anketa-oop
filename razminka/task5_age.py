# Задание 5. Своё исключение


class AgeError(Exception):
    """Возраст вне допустимых границ."""


class Person:
    MIN_AGE = 0
    MAX_AGE = 120

    def __init__(self, fio, age):
        if not self.MIN_AGE <= age <= self.MAX_AGE:
            raise AgeError(
                f"возраст {age} вне границ {self.MIN_AGE}..{self.MAX_AGE}"
            )
        self.fio = fio
        self.age = age


if __name__ == "__main__":
    data = [("Иванов Иван", 19), ("Петрова Анна", 200),
            ("Сидоров Пётр", -5)]
    accepted = []
    for fio, age in data:
        try:
            accepted.append(Person(fio, age))
        except AgeError as error:
            print(f"Не принято: {fio} — {error}")
    print()
    print(f"Принято: {len(accepted)}")
    for p in accepted:
        print(f"  {p.fio}, {p.age} лет")
