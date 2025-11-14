def anagram(string_1, string_2):
    string_1 = sorted(string_1.lower().replace(' ', ''))
    string_2 = sorted(string_2.lower().replace(' ', ''))
    string_1 = "".join(sorted(string_1))
    string_2 = "".join(sorted(string_2))
    if len(string_1) == len(string_2) and string_1 == string_2:
        return True
    else:
        return False

