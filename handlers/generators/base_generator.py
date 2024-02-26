from abc import ABC, abstractmethod

from handlers.handler_interface import HandlerInterface
from models.request import Request


class BaseGenerator(HandlerInterface):
    """
    Base class for all generators. Generators are handlers that are responsible for generating the data.
    """

    def __init__(self, column_name, next_handler=None):
        super().__init__(next_handler)
        self.next_handler = next_handler
        self.column_name = column_name

    @abstractmethod
    def handle(self, request: Request):
        pass

    @abstractmethod
    def generate_data(self, request: Request):
        """
        Generate the data. This method is called by the handle method.
        :param request:
        :return:
        """
        pass
