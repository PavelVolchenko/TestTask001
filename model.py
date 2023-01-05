import sqlite3 as sl


def new_vacancy():
    query = 'INSERT INTO VACANCY (id, name_vacancy, key_skills, description, salary, type_work) ' \
            'values(?, ?, ?, ?, ?, ?)'
    data = [
        (connect.execute("SELECT id FROM VACANCY ORDER BY id DESC LIMIT 1").fetchone()[0] + 1,
         input(" -> Название вакансии: "),
         input(" -> Ключевые навыки: "),
         input(" -> Описание: "),
         int(input(" -> Зарплата: ")),
         input(" -> Тип работы: "))
    ]
    with connect:
        connect.executemany(query, data)


def show_vacancy():
    name = input(" -> Название вакансии: ")
    with connect:
        data = connect.execute(f"SELECT * FROM VACANCY WHERE name_vacancy LIKE '%{name}%'")
        for row in data:
            print(row)


connect = sl.connect('vacancy.sqlite')
