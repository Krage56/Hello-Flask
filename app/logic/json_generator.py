import copy
import json
import random
import string


def random_str(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))


def gen_rand_dict(lvl, num_keys):
    n = 8
    obj = dict()
    for j in range(num_keys):
        tmp = random_str(n)
        i = lvl
        while i:
            tmp = [random_str(n), copy.deepcopy(tmp)]
            i -= 1
        obj.update({random_str(n): tmp})

    return obj


def get_random_json(lvl, num_keys):
    return json.dumps(gen_rand_dict(lvl, num_keys))
