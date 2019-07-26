from math import floor
import string


def create_short_url(integer):
    """Convert an integer to base62 format"""

    base62 = "{}{}".format(string.digits, string.ascii_letters)
    index = integer % 62
    short_url = base62[index]
    quocient = floor(integer / 62)

    while quocient:
        index = quocient % 62
        quocient = floor(quocient / 62)
        short_url = base62[int(index)] + short_url

    return "{}.{}".format('7gs', short_url)
