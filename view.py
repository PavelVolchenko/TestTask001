def show_menu() -> int:
    print("\n\t" + "=" * 12 + " МЕНЮ " + "=" * 12)
    print("\t1. Добавить вакансию")
    print("\t2. Поиск вакансии")
    print("\t9. Закончить работу")
    return int(input(" -> Введите номер необходимого действия: "))
