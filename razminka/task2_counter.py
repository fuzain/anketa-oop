# Задание 2. Класс Counter


class Counter:
    def __init__(self, name):
        self.name = name
        self.value = 0

    def add(self, n=1):
        self.value += n

    def reset(self):
        self.value = 0

    def __str__(self):
        return f"{self.name}: {self.value}"


if __name__ == "__main__":
    accepted = Counter("принято")
    rejected = Counter("отклонено")
    accepted.add(5)
    accepted.add()
    accepted.add()
    rejected.add()
    print(accepted)
    print(rejected)
    accepted.reset()
    print("после сброса:", accepted)
