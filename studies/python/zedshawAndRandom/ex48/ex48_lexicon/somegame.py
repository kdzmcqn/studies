from lexicon import scan
from ex48_lexicon.parser import parse_sentence

action_in = input(">> ")
action_que = scan(action_in)
action_take = parse_sentence(action_que)
print(action_que)
print(action_take)


