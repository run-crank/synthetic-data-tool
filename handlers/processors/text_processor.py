
from handlers.processors.base_processor import BaseProcessor


class TextProcessor(BaseProcessor):
    def __init__(self, regex_key):
        super().__init__(regex_key)

    def get_data(self):
        data = self.data[self.shuffled_index[self.index]]
        self.index = (self.index + 1) % len(self.data)
        return data
