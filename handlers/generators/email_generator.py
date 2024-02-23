import pandas as pd

from enums.regex_keys import RegexKeys
from handlers.generators.base_generator import BaseGenerator
from models.request import Request
from helpers.date_helper import DateHelper


class EmailGenerator(BaseGenerator):
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

    def generate_data(self, request: Request):
        domain = "@thisisjust.atomatest.com"
        test_name = request.test_name
        data = [f"{test_name}{i}_{DateHelper.get_timestamp()}{domain}" for i in range(request.size)]
        temp_df = pd.DataFrame(data, columns=[self.column_name])
        request.data = pd.concat([request.data, temp_df], axis=1)
