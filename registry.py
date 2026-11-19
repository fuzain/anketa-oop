# registry.py — журнал анкет: чтение файла, статистика, сохранение
from people import AnketaError, parse_line


class Registry:
    def __init__(self):
        self.people = []
        self.rejected = []
        self.total_lines = 0
        self.empty_lines = 0

    def add(self, person):
        self.people.append(person)

    def load(self, filename):
        """Читает файл. Возвращает False, если файла нет."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
        except FileNotFoundError:
            return False
        self.total_lines = len(lines)
        for num, line in enumerate(lines, 1):
            if line.strip() == "":
                self.empty_lines += 1
                continue
            try:
                self.add(parse_line(line))
            except AnketaError as error:
                self.rejected.append((num, line.strip(), str(error)))
        return True

    def sorted_people(self):
        return sorted(self.people)

    def stats_by_role(self):
        stat = {}
        for p in self.people:
            stat[p.role()] = stat.get(p.role(), 0) + 1
        return stat

    def stats_by_group(self):
        stat = {}
        for p in self.people:
            group = p.group_name()
            if group is not None:
                stat[group] = stat.get(group, 0) + 1
        return stat

    def save_ok(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for p in self.sorted_people():
                f.write(f"{p.role()};{p.fio};{p.mail};"
                        f"{p.full_phone()};{p.extra()}\n")

    def save_errors(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for num, line, reason in self.rejected:
                f.write(f"строка {num}: {reason} | {line}\n")

    def __len__(self):
        return len(self.people)


if __name__ == "__main__":
    reg = Registry()
    print(reg.load("нет_такого_файла.txt"), len(reg))
