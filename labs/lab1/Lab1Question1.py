'''Yamil Galo'''
'''Ketul Polara'''
'''Stuart Simmons'''
'''Natalie Whitehead'''

number = []

for x in range(2000, 3201+1):
    if (x%7==0) and (x%5!=0):
        number.append(str(x))

print(number)
