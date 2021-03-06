import sys

from src.main.util import read_file, create_environment_with_natives
from src.parser import Parser, ParseError


def main(argv):
    """Parse and run any Tiger program"""

    # check for arguments
    try:
        file = argv[1]
    except IndexError:
        print("Expected one file name argument to be passed, e.g. ./tiger-interpreter program.tig")
        return 40

    program_contents = read_file(argv[1])

    # parse input program
    try:
        program = Parser(program_contents, argv[1]).parse()
    except ParseError as e:
        print("Parse failure: %s" % e.to_string())
        return 42

    # evaluate the program
    environment = create_environment_with_natives()
    result = program.evaluate(environment)

    # print the result and exit
    if result:
        print(result.to_string())
    return 0


if __name__ == "__main__":
    code = main(sys.argv)
    sys.exit(code)


def target(*args):
    return main, None
