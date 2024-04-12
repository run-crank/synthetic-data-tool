
# Synthetic Data Tool (SDT)

SDT provides users with the capability to generate random datasets containing predefined tokens such as phone numbers, names, email addresses, and more. Users have the flexibility to specify the size of the dataset according to their requirements.

## Features
- **Random Dataset Generation with Custom Size:** Users can generate datasets containing various predefined tokens such as phone numbers, names, email addresses, etc., and specify the size of the dataset.

- **Text File Processing:** SDT can process text files provided by the user as input. It replaces instances of keys with random data picked from the generated dataset or any dataset provided by the user.

## Local Environment Setup

### Prerequisite

- Install Python >3.9

### Installation

Create virtual envirnoment
```
pip install virtualenv 
virtualenv venv
source venv/bin/activate
```
Install packages
```
pip install -r requirements.txt
```
## CLI Argument Reference

| Argument       | Default Value     | Description                                                                                              |
|----------------|-------------------|----------------------------------------------------------------------------------------------------------|
| `-o`, `--output` | CSV               | The output mode of the program. This is 'csv' by default, but can be set to 'json' as well.            |
| `-i`, `--input`  |                   | The input text file to be parsed and processed. It It supports any text file format that can be parsed by python's built in file reader library.                                                               |
| `-t`, `--test`   | Generic Test Name | The name of the test to be run. If a dataset will be generated, it will be used as a suffix in the output file.                                                                         |
| `-s`, `--size`   | 50                | The size of the random data to be generated; default is 50.                                              |
| `-d`, `--data`   |                   | Existing csv data to be used for the test; if provided, it won't generate random data. The header will be used as the key for text processing / replacement.                       |

## Usage Argument Examples

Generates a dataset of size 100 in csv format
```
python cli.py -o csv -s 100
```
Generate a dataset and use it to process a yaml file
```
python cli.py -i test.crank.yml // outputs processed_test.crank.yml and dataset in csv format
```
Use an existing dataset to process a yaml file
```
python cli.py -i test.crank.yml -d random_dataset.csv // outputs processed_test.crank.yml
```