import math

# Esta función verifica si la entrada es un número entero


def is_an_integer(input_str):
    while True:
        try:
            int(input_str)
            return True
        except ValueError:
            return False


# Funciones Ejercicio 1


def is_a_valid_dni(dni_number):
    if len(dni_number) >= 7 and len(dni_number) <= 8:
        return True
    else:
        return False


# Funciones Ejercicio 2


def last_word_length(input_string):
    words = input_string.strip().split()
    if words:
        return len(words[-1])
    else:
        return 0


# Funciones Ejercicio 3
def generate_member_id(full_name, dni_number):
    names = full_name.strip().split()
    first_name = names[0]
    last_name = names[-1]
    dni_part = dni_number[:3]

    return f"{first_name}{len(last_name)}{dni_part}"


# Funciones Ejercicio 4
def is_multiple(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


# Funciones Ejercicio 5
def average_temperature(max_temperature, min_temperature):
    return (max_temperature + min_temperature) / 2


# Funciones Ejercicio 6
def add_space_after_letter(text):
    result = " ".join(text)
    return result


# Funciones Ejercicio 7
def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum


# Funciones Ejercicio 8
def calculate_area(radius):
    area = math.pi * radius**2
    return round(area, 2)


def calculate_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return round(perimeter, 2)


# Funciones Ejercicio 9
def login(username, password, attempts):
    if username == "usuario1" and password == "asdasd":
        return True, attempts
    else:
        attempts += 1
        return False, attempts


# Funciones Ejercicio 10
def apply_discount(shopping_cart, discounts):
    total_price = 0

    for product, price in shopping_cart.items():
        if product in discounts:
            discount = discounts[product]
            discounted_price = price - (price * (discount / 100))
            total_price += discounted_price
        else:
            total_price += price

    return total_price


# Funciones Ejercicio 11
def apply_function_to_list(func, input_list):
    results = []

    for item in input_list:
        result = func(item)
        results.append(result)

    return results


def double_number(number):
    return number * 2


# Funciones Ejercicio 12
def count_word_lengths(phrase):
    words = phrase.split()

    result = {}

    for word in words:
        result[word] = len(word)

    return result


# Funciones Ejercicio 13
def calculate_magnitude(vector):
    sum_of_squares = sum([x**2 for x in vector])
    magnitude = math.sqrt(sum_of_squares)
    return magnitude


# Funciones Ejercicio 14
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


# Funciones Ejercicio 15
def calculate_factorial(number):
    if number == 0:
        return 1
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


# Funciones Ejercicio 16
def calculate_frequency(number, digit):
    frequency = 0
    while number > 0:
        last_digit = number % 10
        if last_digit == digit:
            frequency += 1
        number //= 10
    return frequency


# Funciones Ejercicio 17
def calculate_digit_sum(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum
