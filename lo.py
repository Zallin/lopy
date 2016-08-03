import argparse

from interpreter import Interpreter


def read_source_from_file(file_path):
    f = open(file_path)
    return filter(lambda sl: sl or False, map(lambda sl: sl.strip(), f.readlines()))


def repl(inp):
    print('lo.py repl mode')
    while True:
        raw_src = input()
        res = inp.interpet(raw_src)
        print(res)


if __name__ == '__main__':
    inp = Interpreter()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file', help='file to interpet', dest='file_path')
    args = parser.parse_args()
    if args.file_path:
        raw_src = " ".join(read_source_from_file(args.file_path))
        res = inp.interpret(raw_src)
        print(res)
    else:
        repl(inp)
