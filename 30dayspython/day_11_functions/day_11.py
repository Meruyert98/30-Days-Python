def fake_bin(x):
    arr = list(x)
    l = ''
    for i in arr:
        if int(i) > 5:
            l += '1'
        else:
            l += '0'
    return l
    
print(fake_bin('45385593107843568'))