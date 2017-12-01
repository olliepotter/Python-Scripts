from time import time


def print_func(i):
    for x in range(1):
        print(x)


def run_time(func, args):
    start = time()
    func(args)
    end = time()

    return end-start


if __name__ == "__main__":
    print(run_time(print_func, 10))
