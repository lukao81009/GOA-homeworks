def fake_bin(x):
    res = ''
    for currentDigit in x:
        if int(currentDigit) < 5:
            res += '0'
        else:
            res += '1'
    return res