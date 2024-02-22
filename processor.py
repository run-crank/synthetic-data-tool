from handlers.handler_interface import HandlerInterface
from models.request import Request
import pandas as pd


class Processor:
    def __init__(self, request: Request):
        self.handler = self.__initialize_handler_chain()
        self.request = request

    def process(self):
        try:
            self.handler.handle(self.request)
        except Exception as e:
            print(f"Error! Could not execute request.\n Error message: {e}")

    def __initialize_handler_chain(self) -> HandlerInterface:
        pass

    def __initialize_request(self):
        if self.request.is_data_provided:
            self.request.data = pd.read_csv(self.request.data)
        else:
            self.request.data = pd.DataFrame()
