

from ciphey import decrypt
from ciphey.iface import Config


def decrypt_with_ai(passphrase: str):
    """
        https://github.com/Ciphey/Ciphey/wiki/Importing-Ciphey
    """
    return decrypt(
        Config().library_default().complete_config(),
        passphrase)

