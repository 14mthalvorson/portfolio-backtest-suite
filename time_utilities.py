# Converts year string YYYY-MM-DD to year decimal YYYY.nn
def date_str_to_year_decimal(s):
    if len(s) != 10:
        print("Error with input length: '%s'" % s)
        exit(1)
    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[8:])
    return round(y + ((m - 1) * 30.4 + d) / 365, 2)
