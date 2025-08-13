def palindrome(string):
    string_1 = string.lower().replace(' ', '')
    string_2 = string_1[::-1]
    string_2 = string_2.lower().replace(' ', '')
    if string_1 == string_2:
        return True
    else:
        return False

