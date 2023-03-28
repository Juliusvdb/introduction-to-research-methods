# picks a random hour for each month of the year spanning 2013-2022

import random
import calendar
from datetime import datetime

def random_hour_on_random_day(month, year):
    last_day_of_month = calendar.monthrange(year, month)[1]
    day = random.randint(1, last_day_of_month)
    hour = random.randint(0, 23)
    return datetime(year, month, day, hour)

def main():
    for year in range(2013, 2023):
        print(f"\nRandom hours for {year}:")
        for month in range(1, 13):
            random_datetime = random_hour_on_random_day(month, year)
            print(f"Month {month}: {random_datetime}")

if __name__ == "__main__":
    main()
