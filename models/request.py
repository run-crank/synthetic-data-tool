class Request:
    """
    Request class to hold the request data from CLI

    Attributes:
    input_file (str): The input file to be parsed and processed
    output_mode (str): The output mode for the random data used
    test_name (str): The name of the test to be run
    size (int): The size of the random data to be generated; default is 50
    data (str): existing data to be used for the test; if provided, don't generate random data
    """
    def __init__(self, input_file=None, output_mode=None, test_name=None, size=50, data=None):
        self.input_file = input_file
        self.output_mode = output_mode
        self.test_name = test_name
        self.size = size
        self.data = data
        self.is_data_provided = data is not None

    def __str__(self):
        return f"Request(input_file={self.input_file}, output_mode={self.output_mode}, test_name={self.test_name}, size={self.size}, data={self.data})"
