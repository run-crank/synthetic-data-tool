from handlers.generators.email_generator import EmailGenerator
from handlers.generators.phone_generator import PhoneGenerator
from handlers.generators.word_generator import WordGenerator
from handlers.generators.name_generator import NameGenerator
from handlers.output_handler import OutputHandler
from handlers.handler_interface import HandlerInterface
from handlers.processors.process_handler import ProcessHandler
from models.request import Request
from helpers.date_helper import DateHelper
import pandas as pd


class HandlerInitializer:
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
        word_generator = WordGenerator()
        name_generator = NameGenerator()
        email_generator = EmailGenerator()
        phone_generator = PhoneGenerator()
        output_handler = OutputHandler()
        process_handler = ProcessHandler()

        # Common code for both branches
        word_generator.set_handler(name_generator)
        name_generator.set_handler(email_generator)
        email_generator.set_handler(phone_generator)
        phone_generator.set_handler(output_handler)

        if self.request.input_file is not None and not self.request.is_data_provided:
            output_handler.set_handler(process_handler)
            return word_generator
        elif self.request.input_file is None and not self.request.is_data_provided:
            return word_generator
        else:
            return process_handler

    def __initialize_request(self):
        if self.request.is_data_provided:
            self.request.data = pd.read_csv(self.request.data)
        else:
            timestamp = DateHelper.get_timestamp()
            data = [f"{i}_{timestamp}" for i in range(1, self.request.size + 1)]
            temp_df = pd.DataFrame(data, columns=["UID"])
            self.request.data = temp_df
