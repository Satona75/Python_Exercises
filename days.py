def return_day(day):
    days = {1:'sunday',2:'monday',3:'tuesday',4:'wednesday',5:'thursday',6:'friday',7:'saturday'}
    if day in range(1,8):
        return days.get(day)
    else:
        return None

print(return_day(10))



