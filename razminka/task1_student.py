# Задание 1. Класс Student


class Student:
    def __init__(self, fio, group):
        self.fio = fio
        self.group = group

    def short(self):
        """«Иванов Иван Петрович» -> «Иванов И. П.»"""
        words = self.fio.split()
        result = words[0]
        for word in words[1:]:
            result += f" {word[0]}."
        return result


if __name__ == "__main__":
    first = Student("Иванов Иван Петрович", "09с33")
    second = Student("Петрова Анна", "09с34")
    print(first.fio)
    print(first.group)
    print(first.short())
    print(f"{second.short()} | {second.group}")
