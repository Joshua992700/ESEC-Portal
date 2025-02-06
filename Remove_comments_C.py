import sys

def remove_comments(c_code):
    in_single_line_comment = False
    in_multi_line_comment = False
    result = []
    i = 0
    while i < len(c_code):
        if in_single_line_comment and c_code[i] == '\n':
            in_single_line_comment = False
            result.append(c_code[i])
        elif in_multi_line_comment and c_code[i:i+2] == '*/':
            in_multi_line_comment = False
            i += 1  # Skip '*'
        elif not in_single_line_comment and not in_multi_line_comment:
            if c_code[i:i+2] == '//':
                in_single_line_comment = True
                i += 1  # Skip '/'
            elif c_code[i:i+2] == '/*':
                in_multi_line_comment = True
                i += 1  # Skip '*'
            else:
                result.append(c_code[i])
        i += 1
    return ''.join(result)

# Read entire C program input from standard input
c_code = sys.stdin.read()

clean_code = remove_comments(c_code)
print(clean_code)
