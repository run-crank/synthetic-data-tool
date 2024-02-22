from handlers.handler_interface import HandlerInterface
from models.request import Request
from enums.output_mode import OutputMode
from helpers.date_helper import DateHelper


class OutputHandler(HandlerInterface):
    """
    Handler for outputting the generated data to a file.
    """
    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, request: Request):
        timestamp = DateHelper.get_timestamp()
        filename = f"{request.test_name}_{timestamp}"
        if request.output_mode == OutputMode.CSV.value:
            request.data.to_csv(f"{filename}.csv", index=False)
        elif request.output_mode == OutputMode.JSON.value:
            request.data.to_json(f"{filename}.json", orient="records", index=False)
        else:
            raise ValueError("Invalid output mode provided.")

        if self.next_handler is not None:
            self.next_handler.handle(request)
        else:
            return
