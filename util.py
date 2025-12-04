import unicodedata
import re


def format_key_for_auto(key: str) -> str:
    """
    Formats a string key to conform to specific naming conventions:
    - Converts to uppercase
    - Removes colons
    - Collapses multiple spaces into a single space
    - Replaces spaces with underscores
    - Removes accents and non-ASCII characters
    - Removes non-alphanumeric characters except underscores
    - Removes leading and trailing underscores

    :param key: The input string key to format
    :return: The formatted string key
    """
    # Uppercase
    retorno = key.upper()
    # Remove colons
    retorno = retorno.replace(":", "")
    # Collapse multiple spaces
    for _ in range(3):
        retorno = retorno.replace("  ", " ")
    # Replace spaces with underscores
    retorno = retorno.replace(" ", "_")
    # Remove accents/non-ASCII
    retorno = unicodedata.normalize('NFD', retorno)
    retorno = retorno.encode('ascii', 'ignore').decode('ascii')
    # Remove non-alphanumeric/underscore
    retorno = re.sub(r'[^a-zA-Z0-9_]', '', retorno)
    # Remove trailing underscore
    retorno = re.sub(r'[_]$', '', retorno)
    # Remove leading underscore
    retorno = re.sub(r'^[_]', '', retorno)
    return retorno
