import string
import winsound
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from abc import ABC, abstractmethod
from datetime import datetime
import pyttsx3
from functools import reduce
import matplotlib.pyplot as plt

def combine_coins2(coin, numbers):
    return ''.join(list(map(lambda num: coin + str(num) + " ,", numbers)))


# ex 1.1.2
def double_letter(my_str):
    return "".join(list(map(lambda l: l + l, my_str)))


# ex 1.1.3
def four_dividers(number):
    return list(filter(lambda num: num % 4 == 0, range(1, number)))


# ex 1.1.4
def sum_of_digits(number):
    return reduce(lambda x, y: int(x) + int(y), str(number))


# ex 1.3.1
def intersection(list_1, list_2):
    return reduce(lambda acc, val: acc + [val] if val in list_2 and val not in acc else acc, list_1, [])


# ex 1.3.2
def is_prime(number):
    return number > 1 and reduce(lambda acc, val: acc and bool(number % val), range(2, int(number), True))


# ex 1.3.3
def is_funny(string):
    return reduce(lambda acc, char: acc and (char == 'h' or char == 'a'), string, True)


# ex 1.3.4
def figure(password):
    return ''.join(list(
        map(lambda l: chr((ord(l) - ord('a') + 2) % 26 + ord('a')) if l not in string.punctuation and l != ' ' else l,
            password)))


# ex 2.2.2 + ex 2.3.3
class Dog:
    _count_animals = 0

    def __init__(self, age, name="Octavio"):
        self._name = name
        self._age = age
        Dog._count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    @classmethod
    def get_count_animals(cls):
        return cls._count_animals


# ex 2.3.4
class Pixel:
    """
    _x - x coordinate
    _y - y coordinate
    _red - a value between 0 and 255
    _green - a value between 0 and 255
    _blue - a value between 0 and 255
    """

    def __init__(self):
        self._x = 0
        self._y = 0
        self._red = 0
        self._green = 0
        self._blue = 0

    def __init__(self, x, y, red):
        self._x = x
        self._y = y
        self._red = red
        self._green = 0
        self._blue = 0

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        color = f'({self._red}, {self._green}, {self._blue})'
        if self._red == 0 and self._green == 0 and self._blue > 50:
            color += ' Blue'
        elif self._red == 0 and self._blue == 0 and self._green > 50:
            color += ' Green'
        elif self._green == 0 and self._blue == 0 and self._red > 50:
            color += ' Red'
        print(f'X: {self._x}, Y: {self._y}, Color: {color}')


# ex 2.4.2
class BigThing:
    def __init__(self, thing):
        self._thing = thing

    def size(self):
        if isinstance(self._thing, (int, float)):
            return self._thing
        else:
            return len(self._thing)


class BigCat(BigThing):
    def __init__(self, thing, weight):
        super().__init__(thing)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"


# ex 3.1.3
def raise_stop_iteration():
    i = iter([1, 2, 3])
    next(i)
    next(i)
    next(i)
    next(i)


def raise_zero_division_error():
    a = 1
    b = 0
    c = a / b


def raise_assertion_error():
    x = 10
    y = 5
    assert x < y, "AssertionError: x is not less than y"


# def raise_import_error():
#     import non_existent_module


def raise_key_error():
    my_dict = {"key": "value"}
    print(my_dict["non_existent_key"])


# def raise_syntax_error():
#     len('hello') = 5


# def raise_indentation_error():
#         print("IndentationError function")
#             print("IndentationError function - IndentationError")


def raise_type_error():
    a = "5"
    b = 2
    c = a + b


# ex 3.2.5
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return f"__CONTENT_START__\n{content}__CONTENT_END__\n"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__\n"


# ex 3.3.2
class UnderAge(Exception):
    def __str__(self):
        return "Your age is less than 18. You're only " + str(
            self.args[0]) + " years old. Come back in a few years for Ido's birthday."


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


# ex 4.1.2
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return ' '.join(words.get(word, word) for word in sentence.split())


# ex 4.1.3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generate_primes(start):
    current = start
    while True:
        if is_prime(current):
            yield current
        current += 1


def first_prime_over(n):
    primes = generate_primes(n + 1)
    return next(primes)


# ex 4.2.2
def parse_ranges(ranges_string):
    # First generator: split ranges string and convert ranges to (start, stop) tuples
    range_tuples = ((start, stop) for start, stop in (range_str.split('-') for range_str in ranges_string.split(',')))

    # Second generator: generate all numbers in each range
    numbers = (num for start, stop in range_tuples for num in range(int(start), int(stop) + 1))

    return numbers


# ex 4.3.4
def get_fibo():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second


# ex 5.1.2
def sing():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    all_the = notes.split('-')
    print(type(all_the))
    print(all_the)
    for item in all_the:
        both = item.split(',')
        frequency = freqs[both[0]]
        duration = int(both[1])
        winsound.Beep(frequency, duration)


# ex 5.2.2
def good():
    numbers = iter(list(range(1, 101, 3)))
    for i in numbers:
        print(i)


# ex 5.3.2
class MusicNotes:
    def __init__(self):
        self._notes = {
            'La': [55, 110, 220, 440, 880],
            'Si': [61.74, 123.48, 246.96, 493.92, 987.84],
            'Do': [65.41, 130.82, 261.64, 523.28, 1046.56],
            'Re': [73.42, 146.84, 293.68, 587.36, 1174.72],
            'Mi': [82.41, 164.82, 329.64, 659.28, 1318.56],
            'Fa': [87.31, 174.62, 349.24, 698.48, 1396.96],
            'Sol': [98, 196, 392, 784, 1568]
        }
        self._notes_list = []
        for octave in range(5):
            for note in self._notes:
                self._notes_list.append((note, octave))
        self._index = 0
        self._max_index = len(self._notes_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._max_index:
            note, octave = self._notes_list[self._index]
            freq = self._notes[note][octave]
            self._index += 1
            return freq
        else:
            raise StopIteration


# ex 6.1.3
def gui():
    # Let's create the Tkinter window
    window = tkinter.Tk()
    window.title("GUI")
    tkinter.Label(window, text="What do I like the most?", font=("Arial", 14), fg="red").pack()

    # creating a function called DataCamp_Tutorial()
    def DataCamp_Tutorial():
        label = tkinter.Label(window, text="This is what I like:")
        label.pack()
        image = Image.open(r'C:\Users\user\Desktop\sigit\yumi.jpg')
        photo_image = ImageTk.PhotoImage(image)
        image_label = ttk.Label(window, image=photo_image)
        image_label.image = photo_image  # store a reference to the image to prevent garbage collection
        image_label.pack()

    tkinter.Button(window, text="Click Me to find out !", command=DataCamp_Tutorial).pack()
    window.mainloop()


# ex 6.3.3
def text_to_speech():


    # The text that you want to convert to speech
    my_text = "first time i'm using a package in next.py course"

    # Initialize the Text-to-speech engine
    engine = pyttsx3.init()

    # Set the speed of speech
    engine.setProperty('rate', 150)

    # Convert text to speech
    engine.say(my_text)

    # Play the speech
    engine.runAndWait()

#unit1
# ex1- print the longest name
def max_word_in_file():
    with open(r'C:\Users\user\Desktop\sigit\names.txt') as file_input: print(
        max((line.strip() for line in file_input), key=len))


# ex2- print the sum lengths
def sum_lengths():
    with open(r'C:\Users\user\Desktop\sigit\names.txt') as file_input: print(
        sum(len(line.strip()) for line in file_input))


# ex3- print the min names
def min_word_in_file():
    with open(r'C:\Users\user\Desktop\sigit\names.txt') as f:
        lines = [line.strip() for line in f]
        shortest_length = len(min(lines, key=len))
        list(map(lambda line: print(line), filter(lambda line: len(line) == shortest_length, lines)))


# ex4- create length file
def lengths_file():
    with open(r'C:\Users\user\Desktop\sigit\names.txt') as f, open(
            r'C:\Users\user\Desktop\sigit\name_length.txt', 'w') as out_f:
        out_f.writelines(str(len(line.strip())) + "\n" for line in f)


# ex5- names in certain length
def names_in_len():
    name_length = int(input("Enter name length: "))
    with open(r'C:\Users\user\Desktop\sigit\names.txt') as f:
        list(
            map(lambda line: print(line.strip()), filter(lambda line: len(line.strip()) == name_length, f.readlines())))

#unit2
class Animal(ABC):
    zoo_name = "Hayaton"

    # create an animal instance
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    # return the name
    def get_name(self):
        return self._name

    # return if the animal is hungry
    def is_hungry(self):
        return self._hunger > 0

    # feed the animal
    def feed(self):
        self._hunger = self._hunger - 1

    # create an abstract method
    @abstractmethod
    def talk(self):
        pass


class Dog(Animal, ABC):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    # talk method
    def talk(self):
        print('woof woof')

    def fetch_stick(self):
        print('There you go, sir!')


class Cat(Animal, ABC):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    # talk method
    def talk(self):
        print('meow')

    def chase_laser(self):
        print('Meeeeow')


class Skunk(Animal, ABC):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    # talk method
    def talk(self):
        print('tsssss')

    def stink(self):
        print('Dear lord!')


class Unicorn(Animal, ABC):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    # talk method
    def talk(self):
        print('Good day, darling')

    def sing(self):
        print('I’m not your toy...')


class Dragon(Animal, ABC):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    # talk method
    def talk(self):
        print('Raaaawr')

    def breath_fire(self):
        print('$@#$#@$')

# unit3
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_char, index):
        self._message = f"The username contains an illegal character '{illegal_char}' at index {index}"
        super().__init__(self._message)
        self._illegal_char = illegal_char
        self._index = index


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username consists of less than 3 characters"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username consists of more than 16 characters"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The username consists of less than 8 characters"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The username consists of more than 40 characters"


def check_input(username, password):
    try:
        if not is_valid_username(username):
            for index, c in enumerate(username):
                if c not in string.ascii_letters + string.digits + '_':
                    raise UsernameContainsIllegalCharacter(c, index)
            raise UsernameTooShort() if len(username) < 3 else UsernameTooLong()

        if not is_valid_password(password):
            if not any(char.isupper() for char in password):
                raise PasswordMissingUppercase()
            elif not any(char.islower() for char in password):
                raise PasswordMissingLowercase()
            elif not any(char.isdigit() for char in password):
                raise PasswordMissingDigit()
            elif not any(char in string.punctuation for char in password):
                raise PasswordMissingSpecial()
            raise PasswordTooShort() if len(password) < 8 else PasswordTooLong()

        print("OK")
    except Exception as e:
        print(e)


# check if the username valid
def is_valid_username(username):
    legal_chars = string.ascii_letters + string.digits + '_'

    # Check username length
    if len(username) < 3 or len(username) > 16:
        return False

    # Check if all chars are legal
    for c in username:
        if c not in legal_chars:
            return False

    # If all checks pass, return True
    return True


# check if the username valid
def is_valid_password(password):
    # Check password length
    if len(password) < 8 or len(password) > 40:
        return False

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if password contains at least one special character
    if not any(char in string.punctuation for char in password):
        return False

    # If all checks pass, return True
    return True

#unit4

# ex1
def gen_secs():
    """Generator that yields all possible seconds ranges (0-59) - seconds"""
    for s in range(60):
        yield s


# ex2
def gen_minutes():
    """Generator that yields all possible seconds ranges (0-59) - minutes"""
    for s in range(60):
        yield s


# ex3
def gen_hours():
    """Generator that yields all possible seconds ranges (0-59) - hours"""
    for s in range(24):
        yield s


# ex4
def gen_time():
    """Generator that yields all possible times (hour:minutes:second)"""
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h, m, s)


# ex5
def gen_years(start=datetime.now().year):
    """Generator that yields all possible years from given year"""
    year = start
    while True:
        yield year
        year += 1


# ex6
def gen_months():
    """Generator that yields all the months"""
    for m in range(1, 13):
        yield m


# ex7
def gen_days(month, leap_year=True):
    """Generator that yields the number of days in a given month"""
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31,
        4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    days = days_in_month[month]
    return (x for x in range(1, days + 1))


# ex8
def gen_date():
    for year in gen_years():
        # Check if the current year is a leap year
        for month in gen_months():
            # the number of days depend on the given mouth
            for day in gen_days(month, leap_year=(year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield " {}/{}/{} {:02d}:{:02d}:{:02d}".format(day, month, year, hour, minute, second)

#unit5
# ex1
def check_id_valid(id_number):
    """check if the id is current"""
    # convert the int into a list of numbers
    number_list = [int(d) for d in str(id_number)]

    # the first step
    step_one_list = [x * 1 if i % 2 == 0 else x * 2 for i, x in enumerate(number_list)]

    # the second step
    step_two_list = [x % 10 + x // 10 if x > 9 else x for x in step_one_list]

    # sum all the digits
    sum_list = reduce(lambda n, x: n + x, step_two_list)

    return sum_list % 10 == 0


# ex4
def id_generator(start_id):
    """Generator function that yields valid ID numbers in the range (start_id, 999999999)"""
    for i in range(start_id, 1000000000):
        if check_id_valid(i):
            yield i


# ex2
class IDIterator:
    def __init__(self, start_id):
        self._id = int(start_id)
        self._current_id = self._id - 1

    def __iter__(self):
        return self

    def __next__(self):
        self._current_id += 1
        while not check_id_valid(self._current_id):
            self._current_id += 1
        if self._current_id > 999999999:
            raise StopIteration
        return self._current_id


def print_using_gen(input_id):
    print("\nID from generator---->")
    # ex4
    # Create the generator
    gen = id_generator(int(input_id))

    # Iterate over the first 10 values
    for i in range(10):
        print(str(next(gen)))


def print_using_it(input_id):
    # create an iterator
    id_iter = IDIterator(int(input_id))
    print("\nID from iterator---->")
    # Iterate over the first 10 values
    for i in range(10):
        print(str(next(id_iter)))


# ex6
def wanted_print(input_id, print_way):
    """print in the wanted way"""
    if print_way == 'it':
        print_using_it(input_id)
    else:
        print_using_gen(input_id)


#unit6
def find_the_animal():
    # list of dots, in the following format: [x, y, x, y, x, y,...]
    first = (
        146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
        355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
        178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
        307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
        199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
        389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
        216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
        365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
        215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
        290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
        279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
        291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
        306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
        393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
        336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
        259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
        349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
        234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
        339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
        122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
        214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
        134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
        171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
        115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
        89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108,
        132, 110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149,
        77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111,
        156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259,
        136, 266, 139, 276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153,
        366, 149, 379, 147, 394, 146, 399
    )
    second = (
        156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186,
        150, 179, 155, 175, 157, 168, 157, 163, 157, 159, 157, 158, 164, 159, 175,
        159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146,
        218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172,
        114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81,
        162, 77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126,
        113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157,
        128, 156, 134, 157, 136, 156, 136
    )
    image = Image.open("pic.jpg")
    draw = ImageDraw.Draw(image)
    draw.line(first, fill="orange")
    draw.line(second, fill="orange")
    # fill the object
    draw.polygon(first, fill=(255, 0, 0, 128))

    plt.imshow(image)
    plt.show()

    
def main():

    print(combine_coins2('$', range(5)))


if __name__ == '__main__':
    main()