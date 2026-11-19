import math

import pytest

from task1_student import Student
from task2_counter import Counter
from task3_temperature import Temperature
from task4_figures import Circle, Figure, Rect
from task5_age import AgeError, Person


def test_student_short():
    assert Student("Иванов Иван Петрович", "09с33").short() == "Иванов И. П."
    assert Student("Петрова Анна", "09с34").short() == "Петрова А."


def test_students_independent():
    a = Student("Иванов Иван", "09с33")
    b = Student("Петрова Анна", "09с34")
    a.group = "09с35"
    assert b.group == "09с34"


def test_counter():
    c = Counter("принято")
    c.add(5)
    c.add()
    assert str(c) == "принято: 6"
    c.reset()
    assert c.value == 0


def test_counters_independent():
    a, b = Counter("a"), Counter("b")
    a.add(3)
    assert b.value == 0


def test_temperature():
    t = Temperature(21.5)
    assert str(t) == "21.5 C = 70.7 F"
    assert t.fahrenheit == pytest.approx(70.7)
    assert [x.celsius for x in sorted([t, Temperature(-3)])] == [-3, 21.5]
    assert max([t, Temperature(-3)]) is t


def test_figures():
    assert Figure("x").area() == 0
    assert Rect(3, 4).area() == 12
    assert Circle(2).area() == pytest.approx(math.pi * 4)
    assert str(Rect(3, 4)) == "Прямоугольник: площадь 12.00"


def test_age_ok():
    assert Person("Иванов Иван", 19).age == 19


def test_age_bad():
    for age in (-5, 200):
        with pytest.raises(AgeError):
            Person("Иванов Иван", age)
