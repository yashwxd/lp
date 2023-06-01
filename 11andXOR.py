def perform_operation(string):
    result_and = ''
    result_xor = ''

    for char in string:
        and_result = chr(ord(char) & 127)
        result_and += and_result

        xor_result = chr(ord(char) ^ 127)
        if ord(xor_result) < 32:
            xor_result = '*'
        result_xor += xor_result

    print("AND Result: ", result_and)
    print("XOR Result: ", result_xor)


string = "Hello World"
perform_operation(string)
