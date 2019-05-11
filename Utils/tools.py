from random import choice


def generate_code():
    seeds = "0123456789"
    random_str = []
    for i in range(4):
        random_str.append(choice(seeds))
    return "".join(random_str)
