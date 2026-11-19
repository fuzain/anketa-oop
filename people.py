# people.py — классы анкет: Person, Student, Teacher


class AnketaError(Exception):
    """Анкета не прошла проверку."""


class Person:
    def __init__(self, fio, mail, phone):
        self.fio = self.check_fio(fio)
        self.mail = self.check_mail(mail)
        self.phone = self.check_phone(phone)

    @staticmethod
    def check_fio(raw):
        words = raw.split()
        if len(words) < 2:
            raise AnketaError("в ФИО меньше двух слов")
        return " ".join(words).title()

    @staticmethod
    def check_mail(raw):
        mail = raw.strip().lower()
        error = AnketaError(f"почта неверная: {raw.strip()}")
        if mail.count("@") != 1:
            raise error
        name, domain = mail.split("@")
        if name == "" or domain == "":
            raise error
        if "." not in domain or domain.startswith(".") \
                or domain.endswith("."):
            raise error
        return mail

    @staticmethod
    def check_phone(raw):
        digits = "".join(ch for ch in raw if ch in "0123456789")
        if len(digits) != 11:
            raise AnketaError(f"в телефоне цифр: {len(digits)}, нужно 11")
        if digits[0] not in "78":
            raise AnketaError("телефон должен начинаться с 7 или 8")
        return "7" + digits[1:]

    def masked_phone(self):
        return f"+7 ({self.phone[1:4]}) ***-**-{self.phone[9:11]}"

    def full_phone(self):
        p = self.phone
        return f"+7 ({p[1:4]}) {p[4:7]}-{p[7:9]}-{p[9:11]}"

    def short_fio(self):
        words = self.fio.split()
        return words[0] + "".join(f" {w[0]}." for w in words[1:])

    def role(self):
        return "не определена"

    def extra(self):
        return ""

    def group_name(self):
        return None

    def __str__(self):
        return f"{self.short_fio()} ({self.role()})"

    def __lt__(self, other):
        return self.fio < other.fio


class Student(Person):
    def __init__(self, fio, mail, phone, group):
        super().__init__(fio, mail, phone)
        self.group = self.check_group(group)

    @staticmethod
    def check_group(raw):
        group = raw.replace(" ", "").lower()
        if group == "":
            raise AnketaError("группа не указана")
        return group

    def role(self):
        return "студент"

    def extra(self):
        return self.group

    def group_name(self):
        return self.group


class Teacher(Person):
    def __init__(self, fio, mail, phone, chair):
        super().__init__(fio, mail, phone)
        self.chair = self.check_chair(chair)

    @staticmethod
    def check_chair(raw):
        chair = " ".join(raw.split())
        if chair == "":
            raise AnketaError("кафедра не указана")
        return chair

    def role(self):
        return "преподаватель"

    def extra(self):
        return self.chair


TYPES = {"s": Student, "t": Teacher}


def parse_line(line):
    """Строка файла -> Student или Teacher, иначе AnketaError."""
    parts = line.split(";")
    if len(parts) != 5:
        raise AnketaError(f"полей {len(parts)}, нужно 5")
    kind = parts[0].strip().lower()
    if kind not in TYPES:
        raise AnketaError(f"неизвестный тип: {parts[0].strip()}")
    return TYPES[kind](*parts[1:])


if __name__ == "__main__":
    print(parse_line("s;иванов иван петрович;a@mail.ru;89211112233;09с33"))
    print(parse_line("t;петров пётр;p@voenmeh.ru;89217654321;Кафедра И9"))
