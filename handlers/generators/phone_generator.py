from random import randint

import pandas as pd

from enums.regex_keys import RegexKeys
from handlers.generators.base_generator import BaseGenerator
from models.request import Request
from helpers.date_helper import DateHelper


class PhoneGenerator(BaseGenerator):
    def __init__(self, next_handler=None):
        super().__init__(RegexKeys.EMAIL.value, next_handler)

    def handle(self, request: Request):
        if not request.is_data_provided:
            self.generate_data(request)
        else:
            raise ValueError("Data already provided. Cannot generate data.")

        if self.next_handler is not None:
            self.next_handler.handle(request)
        else:
            return

    def generate_phone_number(self):
        area_code = randint(200, 999)
        exchange_code = randint(200, 999)
        station_code = randint(0, 9999)
        return f"({area_code})-{exchange_code}-{station_code:04}"

    def generate_data(self, request: Request):
        data = [f"{self.generate_phone_number()}" for _ in range(request.size)]
        temp_df = pd.DataFrame(data, columns=[self.column_name])
        request.data = pd.concat([request.data, temp_df], axis=1)
