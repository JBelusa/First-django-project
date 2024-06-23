from django.utils.crypto import get_random_string


def generate_personid():
    return get_random_string(length=12)
