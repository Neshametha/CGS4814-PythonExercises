'''Yamil Galo'''
'''Ketul Polara'''
'''Stuart Simmons'''
'''Natalie Whitehead'''

def max(a, b, c):
    maximum = a
    
    if b > a:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum

print("\nQuestion 14")
print(str(max(25, 20, 30)))