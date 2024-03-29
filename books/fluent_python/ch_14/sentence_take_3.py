import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence3:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self): # it is generator expression
        for word in self.words:
            yield word
        return