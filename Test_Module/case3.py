def alphabet(string):
    list_1 = list(string)
    list_1.insert(0,list_1[0].upper())
    list_1.pop(1)
    string = "".join(list_1)
    return string

alphabet("hello")