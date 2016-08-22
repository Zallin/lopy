import argparse

from interpreter import Interpreter


def read_source_from_file(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return filter(lambda sl: sl or False, file_content.replace('\n', ''))


def repl(inp):
    print('lo.py repl mode')
    while True:
        raw_src_str = input()
        res = inp.eval(raw_src_str)
        print(res)


if __name__ == '__main__':
    inp = Interpreter()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file', help='file to interpret', dest='file_path')
    args = parser.parse_args()
    if args.file_path:
        raw_src_str = read_source_from_file(args.file_path)
        res = inp.eval(raw_src_str)
        print(res)
    else:
        repl(inp)
