filepath = 'todos.txt'

def get_todos(filepath_arg=filepath):
    """Reads a txt file and returns the items within that file as a list."""
    with open(filepath_arg, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath_arg=filepath):
    """Writes a list into a txt file."""
    with open(filepath_arg, 'w') as file_local:
        file_local.writelines(todos_arg)