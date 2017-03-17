""" Model for aircraft flights """
from pprint import pprint as pp


class Flight:

    def __init__(self, number, aircraft):
        # print(number[:2])
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number  # 1. _ used to avoid name clash with method named ""
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        row_numbers, seat_letters = self._aircraft.seating_plan()

        # print(rows)
        # print(seat_letters)

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ("Invalid seat row {}".format(row_text))

        if row not in row_numbers:
            raise ValueError("Seat {} already occupied".format(row))

        return row, letter

    def allocate_seat(self,seat, passenger):
        row, letter = self._parse_seat(seat)

        # print(letter)
        # print(row_text)
        if self._seating[row][letter] is not None:
            raise ValueError("Invalid row number {}".format(seat))
        self._seating[row][letter] = passenger

    def reallocate_seat(self, from_seat, to_seat):
        """
        Relocate passenger from a seat to another seat
        :param from_seat:
        :param to_seat:
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]


if __name__ == "__main__":
    f = Flight("SN232", Aircraft("G-EUPT", "Airbus 319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat("1A", "Abdur Rahim")
    f.allocate_seat("2A","Kamran Akmal")
    f.allocate_seat("7D", "Rohit Sharma")
    f.allocate_seat("6A", "Abdur Rahim")
    f.allocate_seat("2B", "Kamran Akmal")
    f.allocate_seat("7C", "Rohit Sharma")
    f.allocate_seat("1D", "Abdur Rahim")
    f.allocate_seat("2E", "Kamran Akmal")
    f.allocate_seat("7F", "Rohit Sharma")

    pp(f._seating)

