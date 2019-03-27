"""Auth utils."""
import binascii
import os


def generate_secret(entropy: int = 32) -> str:

    return binascii.hexlify(os.urandom(entropy)).decode('ascii')
