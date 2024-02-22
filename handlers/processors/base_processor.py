from abc import ABC, abstractmethod
import random


class BaseProcessor(ABC):
    def __init__(self, regex_key):
        self.index = None
        self.shuffled_index = None
        self.regex_key = regex_key
        self.data = []

    def set_data(self, data: list):
        self.data = data
        self.shuffled_index = list(range(len(data)))
        random.shuffle(self.shuffled_index)
        self.index = 0
        
    @abstractmethod
    def get_data(self):
        pass
