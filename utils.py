def string_to_bool(value):
    if type(value) == bool:
        return value

    bool_val = False
    if value.lower() == 'true':
        bool_val = True
    return bool_val
