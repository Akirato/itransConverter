###iTrans Convertor

####Test API:
from indicnlp.transliterate.unicode_transliterate import ItransTransliterator
input_text=u'pitL^In'
lang='hi'
x=ItransTransliterator.from_itrans(input_text,lang)
print(x)

####Test Commandline:
python3 itrans_transliterator.py input ITRANS DEVANAGARI

####For more information:
- [For APIs](http://nbviewer.jupyter.org/url/anoopkunchukuttan.github.io/indic_nlp_library/doc/indic_nlp_examples.ipynb)
- [For CommandLine](http://anoopkunchukuttan.github.io/indic_nlp_library/)
