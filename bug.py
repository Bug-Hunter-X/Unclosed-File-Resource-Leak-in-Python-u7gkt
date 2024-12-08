def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some code that processes the file ... 
    # Missing f.close() call
    return

function_with_unclosed_file('my_file.txt')