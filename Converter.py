import argparse


def lower(input):
    output = ""
    for char in input:
        output += char.lower()
    return output


def upper(input):
    output = ""
    for char in input:
        output += char.upper()
    return output


def alternate(input):
    output = ""
    upper = True
    for char in input:
        if char == " ":
            output += char
        elif upper:
            output += char.upper()
            upper = False
        else:
            output += char.lower()
            upper = True
    return output


def reverse(input):
    output = input[::-1]
    return output


def run(args):
    file = ""
    input = ""
    output = ""
    if type(args.inputfile) != type(None):
        file = open(args.inputfile, 'r')
        input = file.read()
        file.close()
    if type(args.string) != type(None):
        input = args.string
    if args.type == 'lower':
        input = lower(input)
    if args.type == 'upper':
        input = upper(input)
    if args.type == 'alternate':
        input = alternate(input)
    if args.reverse:
        input = reverse(input)
    if type(args.outputfile) != type(None):
        file = open(args.outputfile, 'w')
        file.write(input)
    else:
        print(input)


def main():
    parser = argparse.ArgumentParser(prog='converter')
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-inputfile')
    group.add_argument('-string')
    parser.add_argument('type', choices=['lower', 'upper', 'alternate'])
    parser.add_argument('-outputfile')
    parser.add_argument('-reverse', nargs='?', const=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
