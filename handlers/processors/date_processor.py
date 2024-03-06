from datetime import timezone
from handlers.processors.base_processor import BaseProcessor
import dateparser
import re

class DateProcessor(BaseProcessor):
    def __init__(self, regex_key):
        super().__init__(regex_key)

    def get_data(self, matched_regex):
        date_string = re.search(self.regex_key, matched_regex).group(1)
        try:
            parsed_date = dateparser.parse(date_string)
            parsed_date_utc = parsed_date.astimezone(timezone.utc)
            formatted_date = parsed_date_utc.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
            return formatted_date
        except:
            print(f"Error parsing date: {date_string}")