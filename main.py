import datetime


class AmountDataException(ValueError):
    """Класс исключения на проверку кол-ва введенных данных"""
    pass


class CorrectDataException(Exception):
    """Класс исключения на проверку корректности введенных данных"""
    pass


def check_amount_data(data: list) -> None:
    """Функция проверки правильного количества введенных данных"""
    if len(data) < 6:
        raise AmountDataException(
            f'Введено меньше данных, чем требуется!!!')
    elif len(data) > 6:
        raise AmountDataException(
            f'Введено больше данных, чем требуется!!!')


def check_surname(surname: str) -> None:
    """Функция проверки на корректность введеной фамилии"""
    if not surname.isalpha():
        raise CorrectDataException(f'Некорректная Фамилия -> {surname}')


def check_name(name: str) -> None:
    """Функция проверки на корректность введеного имени"""
    if not name.isalpha():
        raise CorrectDataException(f'Некорректное Имя -> {name}')


def check_patronymic(patronymic: str) -> None:
    """Функция проверки на корректность введеного отчества"""
    if not patronymic.isalpha():
        raise CorrectDataException(f'Некорректное Отчество -> {patronymic}')


def check_bday(b_day: str) -> None:
    """Функция проверки на корректность введеной даты рождения"""
    try:
        datetime.datetime.strptime(b_day, '%d.%m.%Y').date()
    except ValueError:
        raise CorrectDataException(f'Некорректная Дата рождения-> {b_day}')


def check_phone(phone: str):
    """Функция проверки на корректность введеного номера телефона"""
    try:
        int(phone)
    except ValueError:
        raise CorrectDataException(f'Некорректный Номер телефона -> {phone}')


def check_gender(gender: str):
    """Функция проверки на корректность введеного пола"""
    if gender not in ['f', 'm']:
        raise ValueError(f'Некорректный Пол -> {gender}')


def input_user_data() -> list:
    """Функция принимает данные от пользователя и возвращает список данных если они корректны"""
    data = list((x.strip()) for x in input(
        'Введите через пробел Фамилию, Имя, Отчество, Дату рождения, Номер телефона и Пол:\n').split(' '))
    check_amount_data(data)
    check_surname(data[0])
    check_name(data[1])
    check_patronymic(data[2])
    check_bday(data[3])
    check_phone(data[4])
    check_gender(data[5])
    return data


def save_user_file(data: list) -> None:
    """Функция записи данных в файл csv"""
    try:
        with open(f'home_work_3/{data[0].title()}.csv', newline='', encoding='utf-8', mode='a') as file:
            file.write(
                f'<{data[0].title()}> <{data[1].title()}> <{data[2].title()}> <{data[3]}> <{data[4]}> <{data[5].lower()}>\n')
            print('Данные успешно сохранены')
    except OSError:
        raise Exception('Ошибка записи')


def read_data(data: list) -> None:
    """Функция считывающая записанные данные нового пользователя"""
    try:
        with open(f'home_work_3/{data[0].title()}.csv', encoding='utf-8', mode='r') as file:
            print(file.readlines()[-1])
    except OSError:
        raise Exception('Ошибка чтения')


def create_user() -> list:
    while True:
        try:
            user_data = input_user_data()
            return user_data
        except (AmountDataException, CorrectDataException) as e:
            print(str(e))


def main():
    try:
        new_user = create_user()
        save_user_file(new_user)
        read_data(new_user)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
