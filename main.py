# main.py — запуск программы и вывод результата
from registry import Registry

FILE_IN = "anketa.txt"
FILE_OK = "ok.txt"
FILE_ERR = "errors.txt"
LINE = "-" * 84


def cut(text, width):
    """Обрезает длинный текст, чтобы таблица не разъезжалась."""
    return text if len(text) <= width else text[:width - 1] + "…"


def print_table(people):
    print(f"{'№':>3}  {'ФИО':<28} {'Роль':<14} "
          f"{'Группа/кафедра':<16} Телефон")
    print(LINE)
    for i, p in enumerate(people, 1):
        print(f"{i:>3}  {cut(p.fio, 28):<28} {p.role():<14} "
              f"{cut(p.extra(), 16):<16} {p.masked_phone()}")
    print(LINE)


def print_rejected(rejected):
    print()
    print(f"Отклонено строк: {len(rejected)}")
    for num, line, reason in rejected:
        print(f"  строка {num}: {reason}")
        print(f"      {line}")


def print_summary(reg):
    print()
    print(f"Всего строк в файле: {reg.total_lines} "
          f"(пустых: {reg.empty_lines})")
    print(f"Принято: {len(reg)} | Отклонено: {len(reg.rejected)}")
    print()
    print("По ролям:")
    for role, count in sorted(reg.stats_by_role().items()):
        print(f"  {role:<16}{count}")
    print()
    print("По группам:")
    for group, count in sorted(reg.stats_by_group().items()):
        print(f"  {group:<16}{count}")


def main():
    reg = Registry()
    if not reg.load(FILE_IN):
        print(f"Файл {FILE_IN} не найден")
        return
    print_table(reg.sorted_people())
    print_rejected(reg.rejected)
    print_summary(reg)
    reg.save_ok(FILE_OK)
    reg.save_errors(FILE_ERR)
    print()
    print(f"Сохранено: {FILE_OK} и {FILE_ERR}")


if __name__ == "__main__":
    main()
