from gendiff.output import gendiff
from gendiff.cli import parse_args


def main():
    args = parse_args()
    data1 = args.first_file
    data2 = args.second_file
    print(gendiff(data1, data2, args.format))


if __name__ == '__main__':
    main()
