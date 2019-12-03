'''Yamil Galo'''
'''Ketul Polara'''
'''Stuart Simmons'''
'''Natalie Whitehead'''

def adding(string):
    if end(string) >= 3:
        if string.endswith("ing"):
            string += "ly"
        else:
            string += "ing"
    return string