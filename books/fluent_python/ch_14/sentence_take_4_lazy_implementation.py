import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence3:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self): # this is generator function as it yields some value
        for match in RE_WORD.finditer(self.text):
            yield match.group()

