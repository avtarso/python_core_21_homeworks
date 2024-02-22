from datetime import date, datetime


def get_birthdays_per_week(users):

    result = {}
    TODAY = date.today()
    NEWYEAR = datetime(TODAY.year, 12, 26).date()

    for i in users:
        birthday = i["birthday"]
        delta = NEWYEAR - TODAY
        if delta.days <= 0 and i["birthday"].timetuple()[7] <= 6:
            birthday = birthday.replace(year=TODAY.year + 1)
        else:
            birthday = birthday.replace(year=(TODAY.year))
        delta = birthday - TODAY
        if delta.days > -1 and delta.days < 7:
            dd = birthday.timetuple()
            birthday_week_day = birthday.strftime('%A')
            if birthday_week_day == 'Saturday' or birthday_week_day == 'Sunday':
                birthday_week_day = 'Monday'
            try:
                result[birthday_week_day].append(i["name"])
            except KeyError:
                result[birthday_week_day] = [i["name"]]       

    users = result

    # Реалізуйте тут домашнє завдання
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
