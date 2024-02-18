import sys


def summer(*args): return sum(args)


if __name__ == "__main__":

    numbers = [float(arg) for arg in sys.argv[1:]]
    
    print(summer(*numbers))

# python3 hw_2\source\my_sum_argv.py 1 2 3 4 5