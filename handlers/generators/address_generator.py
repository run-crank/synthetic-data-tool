import pandas as pd

from enums.regex_keys import RegexKeys
from handlers.generators.base_generator import BaseGenerator
from models.request import Request
from random_address import real_random_address


class AddressGenerator(BaseGenerator):
    def __init__(self, next_handler=None):
        super().__init__(RegexKeys.ADDRESS.value, next_handler)

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
        addresses = [real_random_address() for _ in range(request.size)]
        data =[]
        for i in range(len(addresses)):
            address_str = f"{addresses[i]['address1']}, {addresses[i]['city']}, {addresses[i]['state']}, {addresses[i]['postalCode']}"
            data.append(address_str)
        temp_df = pd.DataFrame(data, columns=[self.column_name])
        request.data = pd.concat([request.data, temp_df], axis=1)