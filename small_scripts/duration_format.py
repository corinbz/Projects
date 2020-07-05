def format_duration(seconds):
    sec = seconds % 60
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365

    minutes_new = minutes % 60
    hours_new = hours % 24
    days_new = days % 365
    years_new = years

    units = [years_new, days_new, hours_new, minutes_new, sec]

    name_units_multimple = [" years", " days", " hours", " minutes", " seconds"]
    name_units_single = [" year", " day", " hour", " minute", " second"]
    result = []
    comma = ", "
    for i in range(len(units)):
        if units[i] == 1:
            result.append(str(units[i]))
            result.append(name_units_single[i])
        elif units[i] > 1:
            result.append(str(units[i]))
            result.append(name_units_multimple[i])

    print(seconds)
    for i in range(len(result) - 4, 0, -2):
        print(i)
        result.insert(i, comma)

    if len(result) > 2:
        and_str = " and "
        result.insert(-2,and_str)

    if seconds == 0:
        return "now"
    else:
        return "".join(result)


print(format_duration(63))