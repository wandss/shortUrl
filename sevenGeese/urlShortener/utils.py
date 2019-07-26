from math import floor
import string


def create_short_url(pk):
    base62 = "{}{}".format(string.digits, string.ascii_letters)
    index = pk % 62
    short_url = base62[index]
    quocient = floor(pk / 62)

    while quocient:
        index = quocient % 62
        quocient = floor(quocient / 62)
        short_url = base62[int(index)] + short_url

    return "{}.{}".format('7gs', short_url)
