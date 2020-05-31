def string_to_bool(value):
    if type(value) == bool:
        return value

    bool_val = False
    if value.lower() == 'true':
        bool_val = True
    return bool_val


def string_to_int(value):
    if type(value) == int or value == None:
        return value

    return int(value)
