def time_conversion(time):
    if time[-2:] == "AM":
        if time[:2] == "12":
            time = "00" + time[2:]
    else:
        if time[:2] != "12":
            time = str(12 + int(time[:2])) + time[2:]
    
    return time[:-2]

if __name__ == "__main__":
    time = input()

    result = time_conversion(time)

    print(result)
