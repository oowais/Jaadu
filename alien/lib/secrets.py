"""This code snippet has been taken from https://github.com/python/cpython/blob/3.7/Lib/secrets.py
The secrets module was introduced in the python standard library in python3.6.
RasPI uses Python3.5, which doesn't have the secrets module.
In order to not add-on Python3.6 just for this small functionality, this code is used in this fashion.
This is not recommended and should be removed in the near future when python3.6+ is used by Raspbian.
"""

import binascii
import os

DEFAULT_ENTROPY = 32


def token_bytes(nbytes=None):
    if nbytes is None:
        nbytes = DEFAULT_ENTROPY
    return os.urandom(nbytes)

def token_hex(nbytes=None):
    return binascii.hexlify(token_bytes(nbytes)).decode('ascii')
