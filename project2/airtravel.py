from pprint import pprint as pp


class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not number[2:].isdigit() and int(number[2:]) <= 9999:
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.
        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.
        Raises:
            ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat rows {}".format(row_text))
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter.
        Args:
            seat: A seat designator such as 12F
        Returns:
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))
        return row, letter


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
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


class AirbusA319:
    def __init__(self, registration):

        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777:
    def __init__(self, registration):

        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boeing 777"

    def seating_plan(self):

        # For simplicity's sake, we ignore complex
        # seating arrangement for first-class
        return range(1, 56), "ABCDEGHJK"


def make_flights():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat('12A', 'Guido van Rossum')
    f.allocate_seat('15F', 'Bjarne Stroustrup')
    f.allocate_seat('15E', 'Anders Hejlsberg')
    f.allocate_seat('1C', 'John McCarthy')
    f.allocate_seat('1D', 'Richard Hickey')
    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat('55K', 'Larry Wall')
    g.allocate_seat('33G', 'Yukihiro Matsumoto')
    g.allocate_seat('4B', 'Brian Kernighan')
    g.allocate_seat('4A', 'Dennis Ritchie')

    return f, g




