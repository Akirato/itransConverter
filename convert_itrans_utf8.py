#! /usr/bin/python

itrans_utf_dict = {}
source = open("Uni_iTrns.txt","rb").readlines()
for line in source:
    utf,itrans = [i.strip() for i in line.split()]
    itrans_utf_dict[itrans] = int(utf)

print len(itrans_utf_dict.keys())
for i in itrans_utf_dict.keys():
    print i,unicode(unichr(itrans_utf_dict[i]))
