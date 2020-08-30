# global variables
# bob =('direction')
# ann = ('north', 'south', 'east', 'west')
# sid = [(bob, ann) for ann in ann]

# class lexicon:
#     def __init__(self, some_words):
#         self.some_words = some_words

lexicon = {'direction':['north', 'south', 'east', 'west'], 'waw':['yey', 1, 'five']}

bip = []
result = []
some = 'west east go north'
splitted = some.split()
lolol = lexicon['direction']
# [item for val in lexicon.values() for item in val]
match = [i for i, j in zip(splitted, lolol) if i == j]
# match = list(set(lolol).intersection(splitted))
# gib = [m for m in lolol if m in match]
for element in splitted:
    if element in lolol:
        bip.append(element)


print('lolol')
print(lolol)
print('splitted')
print(splitted)
print('match')
print(match)
# print('gib')
# print(gib)
print('result')
print(result)


# if __name__ == '__main__':
#     print('waw')

# [item for item in a if item[0] == 1]

# kk = lexicon.keys()
# print(kk)
# a = [item for t in lexicon.values() for item in t]
# print("item fot item...all values ata to\n" + str(a))
# bb = lexicon.values()
# print("lexicon.values()...\n" + str(bb))
# cc = lexicon.items()
# print("lexicon.items()...\n" + str(cc))
# dd = lexicon.get('direction')
# print("lexicon.get('direction')...values lang ng key\n" + str(dd))
# word = 'north'
# for key, value in lexicon.items():
#     if word in value:
#         print(key)








# colors = ['red', 'green', 'blue', 'yellow']
# som = []
# for color in enumerate(colors):
#     som.append(color)
#
# print(som)


# names = ['raymond', 'rachel', 'matthew']
# colors = ['red', 'green', 'blue', 'yellow']
# for name, color in zip(names, colors):
#     print(name, ' --> ', color)
