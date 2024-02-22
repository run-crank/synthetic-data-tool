import argparse

from enums.output_mode import OutputMode
import helpers.constants as constant
from models.request import Request
from processor import Processor


def setup_request_commandline() -> Request:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default=OutputMode.CSV,
                        help="The output mode of the program. This is 'csv' by "
                             "default, but can be set to 'json' as well.")
    parser.add_argument("-i", "--input", help="The input file to be parsed and processed")
    parser.add_argument("-t", "--test", default=constant.GENERIC_TEST_NAME, help="The name of the test to be run")
    parser.add_argument("-s", "--size", type=int, default=constant.DEFAULT_DATA_SIZE,
                        help="The size of the random data to be generated; default is 50")
    parser.add_argument("-d", "--data",
                        help="existing data to be used for the test; if provided, it won't generate random data")

    try:
        args = parser.parse_args()
        request = Request(input_file=args.input, output_mode=args.output, test_name=args.test, size=args.size,
                          data=args.data)
        # print(request)
        check_request_validity(request)

        return request
    except Exception as e:
        print(f"Error! \n{e}")
        quit()


def check_request_validity(request: Request):
    if request.data is not None and request.input_file is None:
        raise ValueError("Data provided without input file. Please provide input file.")


def main():
    request = setup_request_commandline()
    processor = Processor(request)
    processor.process()


if __name__ == '__main__':
    main()
