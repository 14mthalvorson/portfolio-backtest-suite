# Converts year string YYYY-MM-DD to year decimal YYYY.nn
def date_str_to_year_decimal(s):
    if len(s) != 10:
        print("Error with input length: '%s'" % s)
        exit(1)
    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[8:])
    return round(y + ((m - 1) * 30.4 + d) / 365, 2)


# Tries 3 times to get a price near the intended date
def get_price(prices_dict, year_decimal):
    for i in range(3):
        if prices_dict.get(year_decimal + i/100) in prices_dict:
            return prices_dict[year_decimal + i/100]
    return None
