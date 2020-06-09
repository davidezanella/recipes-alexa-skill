from fb_duckling import Duckling


def string_to_bool(value):
    if type(value) == bool:
        return value

    bool_val = False
    if value.lower() == 'true':
        bool_val = True
    return bool_val


def string_to_int(value):
    if type(value) == int or value is None:
        return value

    return int(value)


def duckling_word_to_int(text):
    duckling = Duckling(url="http://localhost", port="9900", locale="en_US")
    res = duckling(text)
    if len(res) > 0:
        return res[0]['value']['value']
    return None
