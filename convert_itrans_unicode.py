import codecs,sys

def get_mapping(fi):
    mapping_file = codecs.open(fi,encoding='utf-8')
    data = mapping_file.readlines()
    mapping = {}
    for i in data:
        mapping[i.split('\t')[1].strip()] = i.split('\t')[0].strip()
    return mapping

def transliterate(mapping,sentence):
    out = sentence
    for i in mapping.keys():
        out = out.replace(i,mapping[i])
    return out    

if __name__ == "__main__":
    mapping = get_mapping('uni.txt')
    script,inp,outp = sys.argv 
    inp_file = codecs.open(inp,encoding='utf-8')
    out_file = codecs.open(outp,"wb",encoding='utf-8')
    out = transliterate(mapping,inp_file.read())
    out_file.write(out)
    out_file.close()
