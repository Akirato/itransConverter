#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs,sys

svar_set = ['आ'.decode('utf-8'),'इ'.decode('utf-8'),'ई'.decode('utf-8'),'उ'.decode('utf-8'),'ऊ'.decode('utf-8'),'ऋ'.decode('utf-8'),'ए'.decode('utf-8'),'ऐ'.decode('utf-8'),'ओ'.decode('utf-8'),'औ'.decode('utf-8')]
def get_mapping(fi):
    special_char = unicode(unichr(0x94D))
    mapping_file = codecs.open(fi,encoding='utf-8')
    data = mapping_file.readlines()
    mapping = {}
    for i in data:
        if i.split('\t')[1].strip()[-1] == 'a'.decode('utf-8'):
            mapping[i.split('\t')[1].strip()[:-1]] = i.split('\t')[0].strip()+special_char
        mapping[i.split('\t')[1].strip()] = i.split('\t')[0].strip()
    return mapping


def transliterate(mapping,matra_mapping,sentence):
    special_char = unicode(unichr(0x94D))
    out,keys = sentence,mapping.keys()
    for ind,i in enumerate(keys):
        try:
            if keys[ind+1]==" " or keys[ind+1]=='\n':
                print i, (mapping[i]+special_char)
                out = out.replace(i,mapping[i])
            else:
                if i in svar_set:
                    out = out.replace(i,matra_mapping[i])
                else:
                    out = out.replace(i,mapping[i])

        except:
            out = out.replace(i,mapping[i])
#        print out
    return out    

if __name__ == "__main__":
    if len(sys.argv)<3:
	print "Needs input and output file as arguments"
    mapping = get_mapping('uni.txt')
    print mapping
    matra_mapping = get_mapping('matra.txt')
    script,inp,outp = sys.argv 
    inp_file = codecs.open(inp,encoding='utf-8')
    out_file = codecs.open(outp,"wb",encoding='utf-8')
    out = transliterate(mapping,matra_mapping,inp_file.read())
    print transliterate(mapping,matra_mapping,"eosaa na hao ik ivalamba$PaI vaayau [sa ËaoQa$PaI maoGa kao ]Da lao jaaya; Parn%au jyaaoM hI Gar".decode('utf-8'))
    out_file.write(out)
    out_file.close()
