import argparse

def fib(n):
    a = 0
    b = 1
    for x in range(n):
        a,b = b, a+b
    return a

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Fibonacci number" + \
                        "you wish to calculate,", type=int)
    args = parser.parse_args()

    result = fib(args.num)
    print(args.num+result)


if __name__=='__main__':
    main()