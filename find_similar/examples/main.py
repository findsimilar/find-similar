"""
Main functions to work with examples
"""
import os
import pathlib
import yaml


YML_FILE_EXTENSION = '.yml'


def path_to_examples():
    """
    Get path to folder with examples
    """
    data_folder_name = 'data'
    examples_dir_path = pathlib.Path(__file__).parent.resolve()
    return os.path.join(examples_dir_path, data_folder_name)


def examples_set():
    """
    Get all examples list
    """
    examples_file_list = os.listdir(path_to_examples())
    result_list = {
        file.replace(YML_FILE_EXTENSION, '')
        for file in examples_file_list if file.endswith(YML_FILE_EXTENSION)
    }
    return result_list


def get_example(name):
    """
    Get example by name
    :name: Example filename (without extension)
    """
    example_file_path = os.path.join(path_to_examples(), f'{name}{YML_FILE_EXTENSION}')
    with open(example_file_path, 'r', encoding='utf-8') as example_file:
        data = yaml.load(example_file, Loader=yaml.Loader)
    return data
