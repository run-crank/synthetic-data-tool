from datetime import datetime

from handlers.word_generator import WordGenerator
from handlers.name_generator import NameGenerator
from handlers.handler_interface import HandlerInterface
from models.request import Request
import pandas as pd


class Processor:
    def __init__(self, request: Request):
        self.request = request
        self.handler = self.__initialize_handler_chain()

    def process(self):
        self.__initialize_request()
        try:
            self.handler.handle(self.request)
        except Exception as e:
            print(f"Error! Could not execute request.\n Error message: {e}")

    def __initialize_handler_chain(self) -> HandlerInterface:
        """
        Initializes the chain of handlers for processing the request.
        """
        if not self.request.is_data_provided:
            word_generator = WordGenerator()
            name_generator = NameGenerator()
            word_generator.set_handler(name_generator)
            return word_generator
        else:
            return None

    def __initialize_request(self):
        if self.request.is_data_provided:
            self.request.data = pd.read_csv(self.request.data)
        else:
            timestamp = int(datetime.now().timestamp())
            data = [f"{i}_{timestamp}" for i in range(1, self.request.size + 1)]
            temp_df = pd.DataFrame(data, columns=["UID"])
            self.request.data = temp_df
