from django.conf import settings

from random import choice, randint
from string import ascii_letters, digits


AVAILABLE_CHARS = ascii_letters + digits
MAX_SIZE = getattr(settings, 'MAXIMUM_LINK_CHARS', 7)
MIN_SIZE = getattr(settings, 'MINIMUM_LINK_CHARS', 4)


def get_random_code() -> str:
    return ''.join([choice(AVAILABLE_CHARS) for _ in range(randint(MIN_SIZE, MAX_SIZE))])


def create_shortened_link(link) -> str:
    random_code = get_random_code()

    link = link.__class__

    if link.objects.filter(short_link=random_code).exists():
        return create_shortened_link(link)

    return random_code



