from datetime import date


def is_leap_year(current):

    if current % 400 == 0 and current % 100 == 0:
        return True
    elif current % 100 == 0:
        return False
    elif current % 4 == 0:
        return True
    else:
        return False
# on every year that is evenly divisible by 4
  # except every year that is evenly divisible by 100
  #   unless the year is also evenly divisible by 400
