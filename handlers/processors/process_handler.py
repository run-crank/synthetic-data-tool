from enums.regex_keys import RegexKeys
from handlers.handler_interface import HandlerInterface
from models.request import Request
from handlers.processors.text_processor import TextProcessor
import re
from handlers.processors.date_processor import DateProcessor


class ProcessHandler(HandlerInterface):
    """
    Handler for processing the input file.
    """

    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.processors_map = {}
        self.regex_keys = []
        self.regex_pattern = ""

    def handle(self, request: Request):
        self.__initialize_attributes(request)

        if request.input_file is None:
            raise ValueError("No input file provided.")

        filedata = ""
        with open(request.input_file, 'r') as file:
            filedata = file.read()

        new_filedata = self.__process_data(filedata, request)

        with open(f"processed_{request.input_file}", 'w') as file:
            file.write(new_filedata)

        if self.next_handler is not None:
            self.next_handler.handle(request)
        else:
            return

    def __process_data(self, file_string, request) -> str:
        result = ''
        start = 0
        for m in re.finditer(self.regex_pattern, file_string):
            matched_regex = m.group()

            if "date" in matched_regex:
                processor = self.processor_map[RegexKeys.DATE.value]
                data = processor.get_data(matched_regex)
            else:
                processor = self.processor_map[matched_regex]
                data = processor.get_data()

            end, new_start = m.span()
            result += file_string[start:end]
            rep = data
            result += rep
            start = new_start
        result += file_string[start:]
        return result

    def __initialize_attributes(self, request: Request):

        processors = []

        for regex_key in request.data.columns:
            if re.match(r"{{.*}}", regex_key):
                temp = TextProcessor(regex_key)
                temp.set_data(request.data[regex_key])
                processors.append(temp)
                
        date_processor = DateProcessor(RegexKeys.DATE.value)
        
        processors.append(date_processor)

        self.regex_keys = [p.regex_key for p in processors]
        self.regex_pattern = r"((" + '|'.join(self.regex_keys) + r"))"
        self.processor_map = {p.regex_key: p for p in processors}
