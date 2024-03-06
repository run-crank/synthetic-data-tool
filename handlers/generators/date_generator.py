import pandas as pd
from handlers.generators.base_generator import BaseGenerator
from helpers.date_helper import DateHelper
from models.request import Request
from enums.regex_keys import RegexKeys


class DateGenerator(BaseGenerator):
    def __init__(self, next_handler=None):
        super().__init__(RegexKeys.DATE.value, next_handler)

    def handle(self, request: Request):
        if not request.is_data_provided:
            self.generate_data(request)
        else:
            raise ValueError("Data already provided. Cannot generate data.")

        if self.next_handler is not None:
            self.next_handler.handle(request)
        else:
            return

    def generate_data(self, request: Request):
        data = [f"{DateHelper.get_random_datetime()}" for i in range(request.size)]
        temp_df = pd.DataFrame(data, columns=[self.column_name])
        request.data = pd.concat([request.data, temp_df], axis=1)