"""
Read txt files and convert lines to python list
"""
def file_to_list_func(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

    return lines


if __name__ == "__main__":
    file_to_list_func()
