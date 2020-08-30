"""
game lexicon
Direction words: north, south, east, west, down, up, left, right, back
Verbs: go, stop, kill, eat
Stop words: the, in, of, from, at, it
Nouns: door, bear, princess, cabinet
Numbers: any string of 0 through 9 characters
"""

stuff = input('> ')
words = stuff.split()

# tuple - list you can't modify inside ()
# creates pair (type, word)

first_word = ('verb', 'go')
second_word = ('direction', ' north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
