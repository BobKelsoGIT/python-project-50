from gendiff.parser import get_data
from gendiff.generator import generate_diff_list
from gendiff.formatter.choose_format import formatted_output


def gendiff(file_path1, file_path2, style="stylish"):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = generate_diff_list(data1, data2)
    return formatted_output(diff, style)
