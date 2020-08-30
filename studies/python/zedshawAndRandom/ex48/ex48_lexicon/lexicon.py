# global vars
lexicon = {'direction':['north', 'south', 'east', 'west'],
           'verb':['go', 'eat', 'eats', 'kill', 'kills'],
           'stop':['the', 'in', 'of', 'to', 'for', 'at', 'into'],
           'noun':['bear', 'princess']
           }

def convert_to_number(q):
    try:
        return int(q)
    except ValueError:
        return None


def all_values():
    lex_vals = lexicon.values()
    flatvals = [item for subvals in lex_vals for item in subvals]
    return flatvals


def scan(take_action):
    result = []
    valsublist = all_values()
    wordsplit = take_action.split()
    for element in wordsplit:
        number = convert_to_number(element)
        if number:
            result.append(('number', number))
        elif element in valsublist:
            for key in lexicon.keys():
                if element in lexicon[key]:
                    result.append((key, element))
        else:
            result.append(('error', element))
    return result


if __name__ == '__main__':

    print('type in some words')
    somewords = input(">> ")
    output = scan(somewords)
    print(output)

