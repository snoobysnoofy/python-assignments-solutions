def check_leap_year(year):
    if year % 100 ==0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        if year % 4 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    return is_leap_year