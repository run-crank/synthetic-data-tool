from datetime import datetime


class DateHelper:
    @staticmethod
    def get_timestamp():
        return int(datetime.now().timestamp())
