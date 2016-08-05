from datetime import timedelta


def add_gigasecond(birthday_datetime):
    gigasecond = 10 ** 9

    gigabirthday = birthday_datetime + timedelta(seconds=gigasecond)
    return gigabirthday