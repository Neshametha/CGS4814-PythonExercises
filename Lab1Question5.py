'''Yamil Galo'''
'''Ketul Polara'''
'''Stuart Simmons'''
'''Natalie Whitehead'''

number = int(input("Enter an integer: "))
divisors_list = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors_list.append(str(i))

print("The divisors of the", number, "are :", ','.join(divisors_list))
print()