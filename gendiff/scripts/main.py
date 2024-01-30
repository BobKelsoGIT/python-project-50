from gendiff.output import generate_diff
from gendiff.cli import parse_args


def main():
    args = parse_args()
    data1 = args.first_file
    data2 = args.second_file
    print(generate_diff(data1, data2, args.format))


if __name__ == '__main__':
    main()
