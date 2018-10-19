def day_of_programmer(year):
    result = '13.09.'+ str(year)
    if year == 1918:
        result = '26.09.1918'
    elif year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            result = '12.09.'+ str(year)
    elif year % 4 == 0:
            result = '12.09.'+ str(year)
    return result

if __name__ == "__main__":
    year = int(input())

    result = day_of_programmer(year)

    print(result)
    