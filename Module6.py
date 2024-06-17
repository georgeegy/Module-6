from datetime import datetime
from datetime import timedelta

# Part 1
import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print("{0}\t{1}".format(item, cost))

# Part 2: subtract 60 sec
new_time = datetime.now() - timedelta(seconds=60)

print(new_time)

# Part 2: add 2 years
new_time = datetime.now() + 2*365*timedelta(days=1)

print(new_time)

# part 3
d = timedelta(days=100, hours=10, minutes=13)
print(d.days, d.seconds, d.microseconds)

# Part 4
datetime_object = datetime.now()


def measurements(inches, feet):
    total_inches = inches + feet*12
    print(f'At {datetime_object} there were {total_inches} inches')


measurements(1, 2)
