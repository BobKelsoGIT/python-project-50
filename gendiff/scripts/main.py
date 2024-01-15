from gendiff import generate_diff, parse_args


def main():
    args = parse_args()
    data1 = args.first_file
    data2 = args.second_file
    print(generate_diff(data1, data2))


if __name__ == '__main__':
    main()
