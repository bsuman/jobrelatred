def format_duration(seconds):
    if seconds == 0:
        return "now"
    elif seconds < 0:
        return "Incorrect Input!"

    outstring = ""
    unit = ""
    # how many seconds make year: # 86,400 seconds  * 365 Days =  31,536,000 seconds = 1 year
    numyear = seconds // 31536000
    if numyear > 0:
        seconds = seconds % 31536000
        if numyear == 1:
            unit = " year"
        else:
            unit = " years"
        outstring = str(numyear) + unit

    # how many seconds make a day: # 3600 * 24 = 86,400 seconds = 1 Day
    numdays = seconds // 86400
    if numdays > 0:
        seconds = seconds % 86400
        if numdays == 1:
            unit = " day"
        else:
            unit = " days"
        if outstring == "":
            outstring = outstring + str(numdays) + unit
        elif seconds > 0:
            outstring = outstring + ", " + str(numdays) + unit
        else:
            outstring = outstring + " and " + str(numdays) + unit

    # how many seconds make a hour: # 60 minutes = 60 * 60 = 3600 seconds = 1 hour
    numhours = seconds // 3600
    if numhours > 0:
        seconds = seconds % 3600
        if numhours == 1:
            unit = " hour"
        else:
            unit = " hours"

        if outstring == "":
            outstring = outstring + str(numhours) + unit
        elif seconds > 0:
            outstring = outstring + ", " + str(numhours) + unit
        else:
            outstring = outstring + " and " + str(numdays) + unit

    # how many seconds make a minute: # 60 seconds = 1 minute
    nummins = seconds // 60
    if nummins > 0:
        seconds = seconds % 60
        if nummins == 1:
            unit = " minute"
        else:
            unit = " minutes"

        if outstring == "":
            outstring = outstring + str(nummins) + unit
        elif seconds > 0:
            outstring = outstring + ", " + str(nummins) + unit
        else:
            outstring = outstring + " and " + str(nummins) + unit

    # how many seconds make a second: # seconds= # second
    if seconds > 0:
        if seconds == 1:
            unit = " second"
        else:
            unit = " seconds"

        if outstring == "":
            outstring = str(seconds) + unit
        else:
            outstring = outstring + " and "+ str(seconds) + unit
    return outstring


if __name__ == '__main__':
    print(format_duration(1))
    print(format_duration(62))
    print(format_duration(120))
    print(format_duration(3600))
    print(format_duration(3662))
