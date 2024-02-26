import pandas as pd

from enums.regex_keys import RegexKeys
from handlers.generators.base_generator import BaseGenerator
from models.request import Request
from random_word import RandomWords


class WordGenerator(BaseGenerator):
    def __init__(self, next_handler=None):
        super().__init__(RegexKeys.WORD.value, next_handler)
        self.generator = RandomWords()

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
        data = [self.generator.get_random_word() for _ in range(request.size)]
        temp_df = pd.DataFrame(data, columns=[self.column_name])
        request.data = pd.concat([request.data, temp_df], axis=1)
