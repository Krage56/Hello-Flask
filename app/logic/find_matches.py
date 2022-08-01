def to_float(v):
    t_val = None
    if v.find(".") != -1:
        try:
            t_val = float(v)
        except ValueError:
            return None
    return t_val


def to_int(v):
    try:
        t_val = float(v)
    except ValueError:
        return None
    return t_val


'''
Пытается преобразовать строку в один из следующих типов данных,
синонимичных базовым типам в json:
3. str
4. int
5. real
6. bool
7. None
'''


def transform_value(val):
    if val[0] == "'" and val[-1] == "'":
        return val[1:-1]
    if val[0] == "\"" and val[-1] == "\"":
        return val[1:-1]
    t_val = to_float(val)
    if not (t_val is None):
        return t_val

    t_val = to_int(val)
    if not (t_val is None):
        return t_val

    if val == "true":
        return True
    if val == "false":
        return False

    if val == "null":
        return None

    return val


def get_matches(val, j_dict):
    res = []
    val = transform_value(val)
    for key, value in j_dict.items():
        if val == value:
            res.append(key)
    return res
