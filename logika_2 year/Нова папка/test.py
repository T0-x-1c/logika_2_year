def convert(summ, UAtoUSorUStoUA, rate):
    if UAtoUSorUStoUA == "1":
        return summ/rate
    elif UAtoUSorUStoUA == '1':
        return summ*rate

summ = int(input())
UAtoUSorUStoUA = str(input())
rate = int(input())
print(convert(summ,UAtoUSorUStoUA,rate))