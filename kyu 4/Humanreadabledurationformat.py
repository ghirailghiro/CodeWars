'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''

def format_duration(seconds):
    #your code here
    stringOfTime = ""
    if seconds == 0:
        return "now"
    if seconds > 0:
        print(seconds)
        listOfOrder = ["y","d","h","m","s"]
        years = 0
        days = 0
        hours = 0
        minutes = 0
        while(seconds>=365*24*60*60):
            seconds -= (365*24*60*60)
            print("primo while")
            years += 1
        while(seconds>=24*60*60):
            seconds -= (24*60*60)
            print("secondo while")
            days += 1
        while(seconds>=60*60):
            seconds -= (60*60)
            print("terzo while")
            hours += 1
        while(seconds>=60):
            seconds -= (60)
            print("quarto while")
            minutes += 1
        print(seconds)
        auxList = []
        if years !=0:
            if years != 1:
                auxList.append(str(years)+" years")
            else:
                auxList.append(str(years)+" year")
        if days !=0:
            if days != 1:
                auxList.append(str(days)+" days")
            else:
                auxList.append(str(days)+" day")
        if hours !=0:
            if hours != 1:
                auxList.append(str(hours)+" hours")
            else:
                auxList.append(str(hours)+" hour")
        if minutes!=0:
            if minutes != 1:
                auxList.append(str(minutes)+" minutes")
            else:
                auxList.append(str(minutes)+" minute")
        if seconds !=0:
            if seconds != 1:
                auxList.append(str(seconds)+" seconds")
            else:
                auxList.append(str(seconds)+" second")
                
        if len(auxList) == 1:
            return auxList[0]
        if len(auxList) == 2:
            return auxList[0]+" "+"and"+" "+auxList[1]
        for i in range(len(auxList)-2):
            stringOfTime += auxList[i]+","+" "
            
            
    return stringOfTime + auxList[len(auxList)-2]+" "+"and"+" "+auxList[len(auxList)-1]