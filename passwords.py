import random
import string


def generate_password(length):
    "Returns all possible passwords of n length"
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
