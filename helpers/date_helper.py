from datetime import datetime, timedelta
import random


class DateHelper:
    @staticmethod
    def get_timestamp():
        return int(datetime.now().timestamp())

    @staticmethod
    def get_random_datetime():
        random_days = random.randint(1, 365)
        random_hours = random.randint(0, 23)
        random_minutes = random.randint(0, 59)
        random_seconds = random.randint(0, 59)
        random_microseconds = random.randint(0, 999999)
        random_datetime = datetime.now() - timedelta(days=random_days, hours=random_hours, minutes=random_minutes,
                                                    seconds=random_seconds, microseconds=random_microseconds)
        return random_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + 'Z'