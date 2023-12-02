import re
from typing import List


class DataLoader:
    def __init__(self, filename: str):
        self.filename = filename

    def load_data(self) -> List[str]:
        with open(self.filename) as file:
            return file.readlines()


class Decoder:
    WORD_DIGIT_MAPPING = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': '4',
        'five': '5e',
        'six': '6',
        'seven': '7n',
        'eight': 'e8t',
        'nine': '9e',
    }
    DIGIT_SEARCH_PATTERN = re.compile(r'\D*(\d)\D*(?:.*(\d))?\D*')

    def digitize_string(self, input_string: str) -> str:
        for word, digit in self.WORD_DIGIT_MAPPING.items():
            input_string = input_string.replace(word, digit)
        return input_string

    def find_first_and_last_digit(self, input_string: str) -> int:
        digitized_string = self.digitize_string(input_string)
        match = self.DIGIT_SEARCH_PATTERN.match(digitized_string)
        first_digit = match.group(1)
        last_digit = match.group(2) or first_digit
        return int(first_digit + last_digit)


class DecoderApp:
    def __init__(self, filename: str, decoder: Decoder):
        self.filename = filename
        self.decoder = decoder

    def decode(self) -> int:
        result = 0
        data_loader = DataLoader(self.filename)
        encoded_data = data_loader.load_data()

        for line in encoded_data:
            decoded_value = self.decoder.find_first_and_last_digit(line)
            result += decoded_value

        return result


if __name__ == '__main__':
    dcdr = Decoder()
    app = DecoderApp(filename="calibration_document.txt", decoder=dcdr)
    print(app.decode())
