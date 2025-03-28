s = 'MCMXCIV'
sum = 0
prevValue = 0
romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for c in s: # for c in s = indice zero do s
    currentValue = romans[c]
    sum += (currentValue - 2 * prevValue) if (currentValue > prevValue) else currentValue 
    prevValue = currentValue
print(sum)

# Se um número anterior for menor que o próximo, subtraímos, ao contrário, somamos normal
