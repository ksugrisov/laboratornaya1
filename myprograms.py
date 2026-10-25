programs = [
    {
        "name": "Вечерние новости",
        "genre": "Новости",
        "days": ["Пн", "Ср", "Пт"],
        "ratings": [8.4, 8.1, 7.9]
    },
    {
        "name": "Утро в городе",
        "genre": "Развлекательная",
        "days": ["Вт", "Чт", "Сб"],
        "ratings": [5.2, 4.8, 6.1]
    },
    {
        "name": "Спорт-обзор",
        "genre": "Спорт",
        "days": ["Ср", "Сб", "Вс"],
        "ratings": [6.5, 7.0, 6.8]
    },
    {
        "name": "Кино по выходным",
        "genre": "Кино",
        "days": ["Пт", "Сб", "Вс"],
        "ratings": [7.4, 8.8, 9.0]
    },
    {
        "name": "Кулинарный час",
        "genre": "Развлекательная",
        "days": ["Пн", "Вт", "Чт"],
        "ratings": [4.1, 3.9, 4.5]
    },
    {
        "name": "Деловая среда",
        "genre": "Аналитика",
        "days": ["Ср", "Чт", "Пт"],
        "ratings": [5.9, 6.3, 6.0]
    }
]


def print_programs(items):
    print(u"Передача".ljust(20), u"Жанр".ljust(18),
          u"Дни эфира".ljust(22), u"Рейтинги".ljust(18))
    for item in items:
        print(item["name"].ljust(20), item["genre"].ljust(18),
              str(item["days"]).ljust(22), str(item["ratings"]).ljust(18))


def filter_by_average(items, min_average):
    """Возвращает передачи, средний рейтинг которых выше заданного."""
    result = []
    for item in items:
        average = sum(item["ratings"]) / len(item["ratings"])
        if average > min_average:
            result.append(item)
    return result


print("Все передачи:")
print_programs(programs)
print()
try:
    threshold = float(input("Введите минимальный средний рейтинг: "))
except ValueError:
    print("Ошибка: необходимо ввести число.")
else:
    print("Передачи со средним рейтингом выше", str(threshold) + ":")
    print_programs(filter_by_average(programs, threshold))
