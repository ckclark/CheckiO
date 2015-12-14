def checkio(data):
    # f'or fun
    # exec "r=s" + "um(data)"
    # return r
    return len(data) and data[0] + checkio(data[1:])
