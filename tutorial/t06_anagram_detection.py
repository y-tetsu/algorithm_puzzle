"""Anagram Detection
"""


class AnagramDetection:
    """solve Anagram Detection by transform-and-concuer"""
    def __init__(self, path):
        with open(path) as f:
            self.wordbook = f.read().split()

    def solve(self):
        """solve"""
        signatured_words = sorted([(self._signature(i), i) for i in self.wordbook])

        print('(wordbook)')
        for word in self.wordbook:
            print(word)

        print('\n(signature)  (word)')
        for signature, word in signatured_words:
            print(f'{signature:12s} {word}')

    def _signature(self, word):
        """get signature from word"""
        return str(''.join(sorted(word)))


AnagramDetection('t06_anagram_detection.txt').solve()
