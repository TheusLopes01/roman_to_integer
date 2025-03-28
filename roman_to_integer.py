romans = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000, 
}

s = 'XVII'
romanoList = list(s)
sum = 0

for i in range(len(romanoList)-1):
    if romans.get(romanoList[i]) < romans.get(romanoList[i+1]):
        sum -= romans.get(romanoList[i])
    else:
        sum += romans.get(romanoList[i])
sum += romans.get(romanoList[-1])
print(sum)

