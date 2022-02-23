import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

def spr():
    s = "ABC"
    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break

def main():
    s = Sentence('"The time has come," the Walrus said,')
    for word in s:
        print(word)
    print(list(s))
    print(s[0])
    print(s[5])
    print(s[-1])

    spr()

if __name__ == '__main__':
    main()