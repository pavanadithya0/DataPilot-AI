import random


def random_price(min_price=50, max_price=5000):
    return round(random.uniform(min_price, max_price), 2)


def random_quantity():
    return random.randint(1, 5)