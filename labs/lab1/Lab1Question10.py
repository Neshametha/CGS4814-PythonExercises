'''Yamil Galo'''
'''Ketul Polara'''
'''Stuart Simmons'''
'''Natalie Whitehead'''

num = int(input("Please enter a number: "))
j = 0

for i in range(2, num // 2 + 1):
    if (a % i == 0):
        j = j + 1
if (j <= 0):
    print("The number is prime.")
else:
    print("The number is not prime.")