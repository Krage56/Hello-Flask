import json
import random
import string


def random_str(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))


def gen_rand_dict(lvl, num_keys):
    n = 8
    if num_keys > 0:
        obj = dict()
    else:
        obj = list()
    #если количество ключей не нулевое
    for _ in range(num_keys):
        tmp = random_str(n)
        i = lvl
        while i:
            tmp = [random_str(n), tmp]
            i -= 1
        if num_keys > 0:
            obj.update({random_str(n): tmp})
        else:
            obj.append(tmp)
    if num_keys > 0:
        return obj
    #если количество ключей ноль - создаём только массив
    tmp = random_str(n)
    for _ in range(lvl):
        tmp = [random_str(n), tmp]
    obj.append(tmp)

    return obj


def get_random_json(lvl, num_keys):
    return json.dumps(gen_rand_dict(lvl, num_keys))
