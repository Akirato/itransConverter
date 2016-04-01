#! /usr/bin/python
"""
itrans_utf_dict = {}
source = open("Uni_iTrns.txt","rb").readlines()
for line in source:
    utf,itrans = [i.strip() for i in line.split()]
    itrans_utf_dict[itrans] = int(utf)

print len(itrans_utf_dict.keys())
for i in itrans_utf_dict.keys():
    print i,unicode(unichr(itrans_utf_dict[i]))
"""
def get_itrans(Id):
    ITRANS = { \
    'R': 0x931, 
    'M': 0x902,
    '.n': 0x902,
    '.m': 0x902,
    'H': 0x903,
    'a': 0x905,
    'A': 0x906,
    'aa': 0x906,
    'i': 0x907,
    'I': 0x908,
    'ii': 0x908,
    'u': 0x909,
    'U': 0x90A,
    'uu': 0x90A,
    'RRi': 0x90B,
    'R^i': 0x90B,
    'RRI': 0x960, # added by Anoop # extension 
    'R^I': 0x960,# added by Anoop # extension 
    'LLi': 0x90C,
    'L^i': 0x90C,
    'LLI': 0x961,# added by Anoop # extension 
    'L^I': 0x961,# added by Anoop # extension 
    '.e': 0x90E,   # added by Anoop # extension 
    'e': 0x90F,
    'ai': 0x910,
    '.o': 0x912,   # added by Anoop # extension 
    'o': 0x913,
    'au': 0x914,
    'k': 0x915,
    'kh': 0x916,
    'g': 0x917,
    'gh': 0x918,
    '~N': 0x919,
    'c': 0x91A,
    'ch': 0x91A,
    'Ch': 0x91B,
    'j': 0x91C,
    'jh': 0x91D,
    '~n': 0x91E,
    'T': 0x91F,
    'Th': 0x920,
    'D': 0x921,
    'Dh': 0x922,
    'N': 0x923,
    't': 0x924,
    'th': 0x925,
    'd': 0x926,
    'dh': 0x927,
    'n': 0x928,
    'p': 0x92A,
    'ph': 0x92B,
    'b': 0x92C,
    'bh': 0x92D,
    'm': 0x92E,
    'y': 0x92F,
    'r': 0x930,
    'l': 0x932,
    'L': 0x933, # added by anoop
    'ld': 0x933, # added by anoop
    'zh': 0x934, # added by anoop # extension
    'v': 0x935,
    'w': 0x935,
    'sh': 0x936,
    'Sh': 0x937,
    's': 0x938,
    'h': 0x939,
    ".a": 0x93D, # avagraha
    'OM': 0x950,
    'AUM': 0x950,
    '.': 0x0964,
    '..': 0x0965,
    '0': 0x0966,
    '1': 0x0967,
    '2': 0x0968,
    '3': 0x0969,
    '4': 0x096A,
    '5': 0x096B,
    '6': 0x096C,
    '7': 0x096D,
    '8': 0x096E,
    '9': 0x096F,
    # non-standard/obsolete iTrans variants still used in texts from 
    # http://sanskrit.gde.to/
    '.h': 0x903,
    'N^': 0x919,
    'shh': 0x937,
    'JN': 0x91E,
     }
    return ITRANS

#itrans_utf_dict = {}
#source = open("Uni_iTrns.txt","rb").readlines()
#for line in source:
#    utf,itrans = [i.strip() for i in line.split()]
#    itrans_utf_dict[itrans] = int(utf)

itrans_utf_dict = get_itrans(1)
print len(itrans_utf_dict.keys())
for i in itrans_utf_dict.keys():
    print i,unicode(unichr(itrans_utf_dict[i]))

