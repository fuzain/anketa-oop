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
