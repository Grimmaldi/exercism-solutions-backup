from datetime import date
import calendar

def meetup_day(year, month, weekday, descriptor):
    '''This function returns the date that meets the requested conditions.'''
    weekdays = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4,
                'Saturday':5, 'Sunday':6}
    valid_descriptors = ['1st', '2nd', '3rd', '4th', '5th', 'teenth', 'last']
    test_weekday = weekdays.get(weekday)


    if descriptor not in valid_descriptors or weekday.title() not in weekdays:
        raise Exception
    elif descriptor.lower() == 'teenth':
        test_day_of_month = 13
        while calendar.weekday(year, month, test_day_of_month) != test_weekday:
            test_day_of_month += 1
        return date(year, month, test_day_of_month)
    elif descriptor.lower() == 'last':
        cal = calendar.Calendar()
        end_day = max(cal.itermonthdays(year, month))
        test_day_of_month = end_day
        while calendar.weekday(year, month, test_day_of_month) != test_weekday:
            test_day_of_month -= 1
        return date(year, month, test_day_of_month)
    else:
        counter_goal = int(descriptor[0])
        try:
            test_day_of_month, week_counter = 1, 0
            while week_counter != counter_goal:
                if (calendar.weekday(year, month, test_day_of_month) == test_weekday):
                    week_counter += 1
                    test_day_of_month += 1
                else:
                    test_day_of_month += 1
            return date(year, month, test_day_of_month - 1)
        except:
            raise Exception