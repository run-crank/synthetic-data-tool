from handlers.base_handler import BaseHandler
from models.request import Request


class Processor:
    def __init__(self):
        self.handler = self.__initialize_handler_chain()

    def process(self, request: Request):
        try:
            self.handler.handle(request)
        except Exception as e:
            print(f"Error! Could not execute request.\n Error message: {e}")

    def __initialize_handler_chain(self) -> BaseHandler:
        pass
