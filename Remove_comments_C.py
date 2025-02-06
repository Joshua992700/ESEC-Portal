import sys

def remove_comments(c_code):
    in_single_line_comment = False
    in_multi_line_comment = False
    in_string = False
    result = []
    i = 0
    
    while i < len(c_code):
        if in_string:
            if c_code[i] == '"' and (i == 0 or c_code[i-1] != '\\'):  # Handle string end
                in_string = False
            result.append(c_code[i])
        
        elif in_single_line_comment and c_code[i] == '\n':
            in_single_line_comment = False
            result.append(c_code[i])  # Keep the newline after single-line comments

        elif in_multi_line_comment and c_code[i:i+2] == '*/':
            in_multi_line_comment = False
            i += 1  # Skip '*' after '*/'

        elif not in_single_line_comment and not in_multi_line_comment:
            if c_code[i:i+2] == '//':  # Start of single-line comment
                in_single_line_comment = True
                i += 1  # Skip '/'
            elif c_code[i:i+2] == '/*':  # Start of multi-line comment
                in_multi_line_comment = True
                i += 1  # Skip '*'
            elif c_code[i] == '"':  # Start of string literal
                in_string = True
                result.append(c_code[i])
            else:
                result.append(c_code[i])
        
        i += 1

    # Join the result into a string and split it into lines
    cleaned_code = ''.join(result).splitlines()

    # Remove any empty lines and return the cleaned code without extra newlines
    cleaned_code = [line for line in cleaned_code if line.strip() != '']
    
    # Join the cleaned lines back into a single string
    return '\n'.join(cleaned_code)


# Read entire C program input from standard input
c_code = sys.stdin.read()

clean_code = remove_comments(c_code)
print(clean_code)
