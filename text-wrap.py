import textwrap

def wrap(string, max_width):
    string_list = list(string)
    wrap_string = ''
    for iter in range(0, len(string), max_width):
        line = ''.join(string_list[iter:iter+max_width])
        wrap_string = wrap_string + line + '\n'
    return wrap_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
