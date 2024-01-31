import json
import yaml
import os


def get_extension(file_path) -> str:
    """
    Get file extension
    """
    _, extension = os.path.splitext(file_path)
    return extension[1:]


def get_data(file_path):
    """
    Load data from file
    """
    if get_extension(file_path) == 'json':
        return json.load(open(file_path))
    elif get_extension(file_path) in ['yml', 'yaml']:
        return yaml.safe_load(open(file_path))
