from abc import ABC, abstractmethod
from models.request import Request


class BaseHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_handler(self, next_handler):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request: Request):
        """
        Handle the request. If successful and next_handler is not None, then
        pass the request to the next handler.
        """
        pass
