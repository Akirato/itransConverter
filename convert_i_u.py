import codecs

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
    print transliterate(mapping,unicode("ilayaa AaOr Pyaar"))
    #for i in mapping.keys():
    #    print i,mapping[i]
    #print len(mapping.keys())
