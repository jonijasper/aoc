def txt2Array(filename):
    file = open(filename, "r")
    t = file.read().splitlines()    # splittaa linet
    file.close()
    return t