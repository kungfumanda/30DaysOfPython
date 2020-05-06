def exponetiate(x, y):
    return x**y


def process_string(name):
    return name.lower().strip()


def organize_data(tup):
    organized = {
        "name": tup[0],
        "nacionality": tup[1],
        "age": tup[2]
    }
    return organized

def is_it_prime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

