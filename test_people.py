import pytest

from people import AnketaError, Person, Student, Teacher, parse_line


def test_person_ok():
    p = Person("  иванов   иВАН петрович ", " IvAnov@Mail.Ru ",
               "+7 (921) 111-22-33")
    assert p.fio == "Иванов Иван Петрович"
    assert p.mail == "ivanov@mail.ru"
    assert p.phone == "79211112233"


def test_fio_one_word():
    with pytest.raises(AnketaError):
        Person("сидоров", "a@mail.ru", "89211112233")


def test_mail_bad():
    for raw in ["kuznetsov.mail.ru", "a@@mail.ru", "a@mail.", "a@.ru",
                "@mail.ru", "a@mail"]:
        with pytest.raises(AnketaError):
            Person.check_mail(raw)


def test_phone_ok():
    assert Person.check_phone("8 921 555 44 33") == "79215554433"


def test_phone_bad():
    for raw in ["+7921123", "99215550000"]:
        with pytest.raises(AnketaError):
            Person.check_phone(raw)


def test_masked_and_short():
    p = Person("иванов иван петрович", "a@mail.ru", "89211112233")
    assert p.masked_phone() == "+7 (921) ***-**-33"
    assert p.short_fio() == "Иванов И. П."
    assert p.role() == "не определена"


def test_lt_sorts_by_fio():
    a = Person("яковлев пётр", "a@mail.ru", "89211112233")
    b = Person("абрамов иван", "b@mail.ru", "89211112233")
    assert sorted([a, b]) == [b, a]


def test_student():
    s = Student("иванов иван", "a@mail.ru", "89211112233", " 09С 33 ")
    assert s.group == "09с33"
    assert s.role() == "студент"
    assert s.extra() == "09с33"


def test_student_empty_group():
    with pytest.raises(AnketaError):
        Student("иванов иван", "a@mail.ru", "89211112233", "  ")


def test_teacher():
    t = Teacher("петров пётр", "p@mail.ru", "89211112233", "Кафедра И9")
    assert t.role() == "преподаватель"
    assert t.extra() == "Кафедра И9"
    assert t.group_name() is None


def test_teacher_empty_chair():
    with pytest.raises(AnketaError):
        Teacher("петров пётр", "p@mail.ru", "89211112233", "")


def test_parse_line_types():
    line = "s;иванов иван;a@mail.ru;89211112233;09с33"
    assert isinstance(parse_line(line), Student)
    line = "t;петров пётр;p@mail.ru;89211112233;Кафедра И9"
    assert isinstance(parse_line(line), Teacher)


def test_parse_line_bad():
    for line in ["x;иванов иван;a@mail.ru;89211112233;что-то",
                 "s;волков денис;volkov@mail.ru;+79219998877"]:
        with pytest.raises(AnketaError):
            parse_line(line)
