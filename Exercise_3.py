hours = int(input('Enter hour:'))
am_pm = int(input('am (1) or pm (2)?'))
hoursToGo = int(input('How many hours ahead?'))

if am_pm == 2:
    hours += 12
hours += hoursToGo
hours %= 24
if hours >= 12:
    hours -= 12
    am_pm = 2

print('New hour: ', hours, 'pm' if am_pm == 2 else 'am')

