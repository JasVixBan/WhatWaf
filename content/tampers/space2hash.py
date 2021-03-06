from lib.settings import random_string


__example_payload__ = "' AND 1=1 OR 2=2"
__type__ = "changing the payload spaces to obfuscated hashes with a newline"


def tamper(payload, **kwargs):
    modifier = "%%23{}%%0A".format(random_string())
    retval = ""
    for char in payload:
        if char == " ":
            retval += modifier
        else:
            retval += char
    return retval
