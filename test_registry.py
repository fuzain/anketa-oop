from people import Student
from registry import Registry

TEXT = """s;иванов иван;a@mail.ru;89211112233;09с33
t;петров пётр;p@mail.ru;89217654321;Кафедра И9

x;непонятный тип;a@b.ru;89211112233;что-то
s;сидоров;s@mail.ru;89210000000;09с34
"""


def make_file(tmp_path):
    path = tmp_path / "anketa.txt"
    path.write_text(TEXT, encoding="utf-8")
    return str(path)


def test_load_missing_file():
    reg = Registry()
    assert reg.load("нет_такого_файла.txt") is False
    assert len(reg) == 0


def test_load(tmp_path):
    reg = Registry()
    assert reg.load(make_file(tmp_path)) is True
    assert len(reg) == 2
    assert len(reg.rejected) == 2
    assert reg.empty_lines == 1
    assert reg.rejected[0][0] == 4


def test_add():
    reg = Registry()
    reg.add(Student("иванов иван", "a@mail.ru", "89211112233", "09с33"))
    assert len(reg) == 1


def test_stats(tmp_path):
    reg = Registry()
    reg.load(make_file(tmp_path))
    assert reg.stats_by_role() == {"студент": 1, "преподаватель": 1}
    assert reg.stats_by_group() == {"09с33": 1}


def test_save(tmp_path):
    reg = Registry()
    reg.load(make_file(tmp_path))
    ok = tmp_path / "ok.txt"
    err = tmp_path / "errors.txt"
    reg.save_ok(str(ok))
    reg.save_errors(str(err))
    assert len(ok.read_text(encoding="utf-8").splitlines()) == 2
    assert len(err.read_text(encoding="utf-8").splitlines()) == 2
