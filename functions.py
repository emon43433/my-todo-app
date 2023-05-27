def write_todos(filepath, todos_arg):
     with open(filepath, 'w') as file_w:
        file_w.writelines(todos_arg)


def get_todos(filepath):
    with open('todos.txt', 'r') as file_r:
        todos = file_r.readlines()
    return todos


# if file is run directly
if __name__ == "__main__":
    print("hello")
