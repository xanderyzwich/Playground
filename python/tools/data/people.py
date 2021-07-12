"""
You’re given a csv of test data, but it’s incomplete.
Fill in missing values (cells with no data) with fake data
In addition to missing values,
    add a phone_number column (with fake phone numbers in the format  (xxx) xxx-xxxx)
    and an unique email_address column (with fake emails)
Uniqueness is paramount for the proposed insertion as a user account credentialOutput a new csv file that’s now complete
"""
import re


class Rando:

    def person_number(self):
        return 52

    def first_name(self):
        return 'fake'

    def last_name(cls):
        return 'name'

    def phone_number(cls):
        return '(555) 867-5309'

    def email_address(cls):
        return 'shallow@fake.com'


class Line:

    def __init__(self, input_line):
        self.person_number, self.first_name, self.last_name = Line.split_line(input_line)
        self.phone_number = Rando.phone_number()
        self.email_address = Rando.email_address()

    def complete_data(self):
        _blank = ''
        if self.person_number == _blank:
            self.person_number = Rando.person_number()
        if self.first_name == _blank:
            self.first_name = Rando.first_name()
        if self.last_name == _blank:
            self.last_name = Rando.last_name()

    @staticmethod
    def _split_line(input_line):
        return [piece.replace('"', '') for piece in re.split(',', input_line)]

    def __repr__(self):
        data = [self.person_number, self.first_name, self.last_name, self.phone_number, self.email_address]
        return ','.join(f'"{piece}"' for piece in data)

# def handle_input(input_line):
#     person_number, first_name, last_name = split_line(input_line)
#     person_number = person_number if person_number is not blank else Rando.person_number()
#     first_name = first_name if first_name is not blank else Rando.first_name()
#     last_name = last_name if last_name is not blank else Rando.last_name()
#     phone_number = Rando.phone_number()
#     email_address = Rando.email_address()
#     return person_number, first_name, last_name, phone_number, email_address


def write_data(output_file, data):
    output_file.write([Rando.add_quotes(piece) for piece in data])


if __name__ == '__main__':
    blank = ''
    with open('people.csv', 'r') as input_file, open('people_complete.csv', 'w') as output_file:
        for line in input_file:
            data = Line(line)
            write_data(output_file, data)
