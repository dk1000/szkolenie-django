from typing import Union


def celsiusz_na_kelvin(celsiusze: Union[int, float]) -> str:
    """
    >>> celsiusz_na_kelvin(0)
    273.15

    >>> celsiusz_na_kelvin(1)
    274.15

    >>> celsiusz_na_kelvin(-1)
    272.15

    >>> celsiusz_na_kelvin(-300)
    Traceback (most recent call last):
        ...
    ValueError: Temperatura w Kelvinach nie może być ujemna

    >>> celsiusz_na_kelvin([1, 2, 3])
    Traceback (most recent call last):
        ...
    TypeError: Argument must be an int or float

    >>> celsiusz_na_kelvin('one')
    Traceback (most recent call last):
        ...
    TypeError: Argument must be an int or float

    >>> celsiusz_na_kelvin({'temp': 10})
    Traceback (most recent call last):
        ...
    TypeError: Argument must be an int or float

    """
    OFFSET = 273.15

    if not isinstance(celsiusze, (int, float)):
        raise TypeError('Argument must be an int or float')

    if OFFSET + celsiusze < 0:
        raise ValueError('Temperatura w Kelvinach nie może być ujemna')

    return float(celsiusze + OFFSET)

import doctest
doctest.testmod()
