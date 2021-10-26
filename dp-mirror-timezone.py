from datetime import timedelta, datetime


def get_schedule(dt):
    '''
    Takes in a UTC datetime, assessing AEST/AEDT and returns a cron schedule

    AEDT = First Sunday in October to the First Sunday in April, AEST outside of this
    AEDT-dp_mirror-UTC = "0 19 * * *"
    AEST-dp_mirror-UTC =  "0 20 * * *"

    :param dt:
    :type datetime
    :return str
    '''

    current_sydney_time = dt + timedelta(hours=10)

    # Check if current time is between the First Sunday of April: 2am and First Sunday of October: 2am
    print(current_sydney_time)
    if current_sydney_time <= next_weekday(datetime(dt.year, 4, 1, 2, 0, 0), 6) or current_sydney_time >= next_weekday(datetime(dt.year, 10, 1, 2, 0, 0), 6):
        return "0 19 * * *"

    return "0 20 * * *"

def next_weekday(d, weekday):
    '''
    Takes a datetime and a weekday (0 = Monday, 6 = Sunday) and returns the date of the next occurrence of this weekday
    :param d:
    :type datetime
    :param weekday:
    :type int
    :return: datetime
    '''
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days_ahead)


########################################################################################################################
#
#
#   Unit Tests
#
#   For 2021:
#   First Sunday of April is 4/4/2021 02:00:00 -> UTC 2021-04-03 16:00:00
#   First Sunday of October is 3/10/2021 02:00:00 -> UTC 2021-10-02 16:00:00
#
########################################################################################################################

# Test April UTC Time
assert get_schedule(datetime(2021, 4, 3, 12, 0, 0)) == "0 19 * * *", "Test 1 - First Sunday of April - AEST 4/4/2021 01:00:00 = UTC 2021-04-03 14:00:00"
assert get_schedule(datetime(2021, 4, 3, 13, 0, 0)) == "0 19 * * *", "Test 2 - First Sunday of April - AEST 4/4/2021 01:00:00 = UTC 2021-04-03 14:00:00"
assert get_schedule(datetime(2021, 4, 3, 14, 0, 0)) == "0 19 * * *", "Test 3 - First Sunday of April - AEST 4/4/2021 01:00:00 = UTC 2021-04-03 14:00:00"
assert get_schedule(datetime(2021, 4, 3, 15, 0, 0)) == "0 19 * * *", "Test 4 - First Sunday of April - AEST 4/4/2021 02:00:00 = UTC 2021-04-03 15:00:00"
assert get_schedule(datetime(2021, 4, 3, 16, 0, 0)) == "0 19 * * *", "Test 5 - First Sunday of April - AEST 4/4/2021 03:00:00 = UTC 2021-04-03 16:00:00"
assert get_schedule(datetime(2021, 4, 3, 17, 0, 0)) == "0 20 * * *", "Test 6 - First Sunday of April - AEST 4/4/2021 03:00:00 = UTC 2021-04-03 16:00:00"
assert get_schedule(datetime(2021, 4, 3, 18, 0, 0)) == "0 20 * * *", "Test 7 - First Sunday of April - AEST 4/4/2021 03:00:00 = UTC 2021-04-03 16:00:00"
assert get_schedule(datetime(2021, 4, 3, 19, 0, 0)) == "0 20 * * *", "Test 8 - First Sunday of April - AEST 4/4/2021 03:00:00 = UTC 2021-04-03 16:00:00"

# Test October UTC Time
assert get_schedule(datetime(2021, 10, 2, 12, 0, 0)) == "0 20 * * *", "Test 9 - First Sunday of October - AEST 2021-10-03 02:00:00 = UTC 2021-10-02 12:00:00"
assert get_schedule(datetime(2021, 10, 2, 13, 0, 0)) == "0 20 * * *", "Test 10 - First Sunday of October - AEST 2021-10-03 02:00:00 = UTC 2021-10-02 15:00:00"
assert get_schedule(datetime(2021, 10, 2, 14, 0, 0)) == "0 20 * * *", "Test 11 - First Sunday of October - AEST 2021-10-03 03:00:00 = UTC 2021-10-02 16:00:00"
assert get_schedule(datetime(2021, 10, 2, 15, 0, 0)) == "0 20 * * *", "Test 12 - First Sunday of October - AEST 2021-10-03 01:00:00 = UTC 2021-10-02 14:00:00"
assert get_schedule(datetime(2021, 10, 2, 16, 0, 0)) == "0 19 * * *", "Test 13 - First Sunday of October - AEST 2021-10-03 01:00:00 = UTC 2021-10-02 14:00:00"
assert get_schedule(datetime(2021, 10, 2, 17, 0, 0)) == "0 19 * * *", "Test 14 - First Sunday of October - AEST 2021-10-03 01:00:00 = UTC 2021-10-02 14:00:00"
assert get_schedule(datetime(2021, 10, 2, 18, 0, 0)) == "0 19 * * *", "Test 15 - First Sunday of October - AEST 2021-10-03 01:00:00 = UTC 2021-10-02 14:00:00"
assert get_schedule(datetime(2021, 10, 2, 18, 0, 0)) == "0 19 * * *", "Test 16 - First Sunday of October - AEST 2021-10-03 01:00:00 = UTC 2021-10-02 14:00:00"