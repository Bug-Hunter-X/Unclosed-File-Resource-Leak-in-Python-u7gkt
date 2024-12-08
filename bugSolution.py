def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            file_content = f.read()
            return file_content
    except FileNotFoundError:
        return None

function_with_closed_file('my_file.txt')
