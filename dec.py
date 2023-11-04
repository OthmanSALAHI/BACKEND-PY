def BinDec(bin):
    Dec = 0
    for i in range(len(bin)):
        if bin[i] == '1':
           Dec += 2 ** i
        elif bin[i] == '0':
            Dec += 0
        else:
            return None
    return Dec

dec = BinDec("101")
print(dec)