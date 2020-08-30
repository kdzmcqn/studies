# from dataclasses import dataclass
from random import choice
from random import randrange


class Character():

    def __init__(self, char_name, char_description, constitution, weapon=None, attack_mod=1.0,
                 max_damage=5, items=None):
        self._name = char_name
        self._description = char_description
        self._constitution = constitution
        self._weapon = weapon
        self._attack_mod = attack_mod
        self._max_damage = max_damage

        if items is None:
            self._items = []
        else:
            self.items = items

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def constitution(self):
        return self._constitution

    @constitution.setter
    def constitution(self, constitution):
        self._constitution = constitution

    @property
    def conversation(self):
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        self._conversation = self.talk(conversation)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def items_names(self):
        return [item.name for item in self.items]

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, weapon):
        self._weapon = weapon

    @property
    def attack_mod(self):
        return self._attack_mod

    @attack_mod.setter
    def attack_mod(self, attack_mod):
        self._attackmod = attack_mod

    @property
    def max_damage(self):
        return self._max_damage

    @max_damage.setter
    def max_damage(self, max_damage):
        self._max_damage = max_damage

    def talk(self, conversation=None):
        if conversation is not None:
            for statement in conversation:
                yield "[{0}]: {1}".format(self.name, statement)
            while True:
                yield "[{0}]: ...".format(self.name)
        else:
            return "{0} doesn't want to talk to you.".format(self.name)

    def attack(self, opponents):

        defender = opponents[0]

        if len(opponents) > 1:
            for opponent in opponents:
                if opponent.constitution > defender.constitution:
                    defender = opponent

        attack_roll = self.roll_dice() * self._attack_mod
        damage_roll = self.roll_dice(1, self.max_damage)

        return (defender, attack_roll, damage_roll, self.weapon)

    def defend(self, attack, damage, weapon):

        defense_roll = self.roll_dice()

        if attack > defense_roll:

            if attack == 20:
                print("Critical Hit! ", end=' ')

                if self.constitution > 6:
                    self.constitution //= 2
                else:
                    self.constitution = 0

            else:
                if isinstance(self, Enemy) and (self.weakness == weapon.name or self.weakness == "any"):
                    damage += 1
                self.constitution -= damage

            if self.constitution > 0 and attack == 20:
                return(True, " reduces {0}'s hitpoints by half. {1} has {2} hitpoints left"\
                       .format(self.name, self.name, self.constitution))

            elif self.constitution > 0:
                return (True, " hits {0} for {1} damage. {2} has {3} hitpoints left."
                        .format(self.name,damage, self.name, self.constitution))

            else:
                return (False, " kills {0}.".format(self.name))

        elif defense_roll - attack > 2:
            return (True, " misses {0}.".format(self.name))

        else:
            return (True, " is blocked by {0}".format(self.name))


    def roll_dice(self, num_dice=1, num_sides=20):

        total = 0

        for die in range(num_dice):
            total += randrange(1, (num_sides +1))
        return total


    def __str__(self):
        return "{0} ({1})".format(self.name, self.description)


class Enemy(Character):

    def __init__(self, char_name, char_description, constitution, weapon=None, attack_mod=1.0,
                 max_damage=5, items=None, weakness='any'):

        super().__init__(char_name, char_description, constitution, weapon, attack_mod,
                         max_damage, items)

        self.weakness = weakness
        self._theft_victim = False

    @property
    def weakness(self):
        return self._weakness

    @weakness.setter
    def weakness(self, weakness):
        self._weakness = weakness

    def steal(self, dice_roll):

        if self.items == []:
            return (None, "{0} has nothing to steal.".format(self.name))

        if self._theft_victim:
            return (None, "{0} has been alerted to your prior theft attempt.".format(self.name))

        if dice_roll > 8:
            item_stolen = choice(self.items)
            self.items.remove(item_stolen)
            self._theft_victim = True
            return (item_stolen, "Item stolen: {0}".format(item_stolen))

        if self.roll_dice(1,8) > 5:
            self._theft_victim = True
            return (None, "You were unsuccessful, and {0} took notice.".format(self.name))


class Friend(Character):

    def __init__(self, char_name, char_description, constitution, weapon=None, attack_mod=1.0,
                 max_damage=5, items=None, in_party=True):

        super().__init__(char_name, char_description, constitution, weapon, attack_mod,
                     max_damage, items)

        self._in_party = in_party

    @property
    def in_party(self):
        return self._in_party

    @in_party.setter
    def in_party(self, true_or_false):
        self._in_party = true_or_false

    def receive_gift(self, gift):

        if gift is not None:
            self.items += [gift,]
            print("\n{0}'s inventory: {1}".format(self.name, ", ".join(self.items_names)))
            print("[{0}]: Thank you. Your kindness will not be soon forgotten.".format(self.name))
        return self.items


class Player(Character):

    def __init__(self, char_name, char_description, constitution, weapon=None,
                 attack_mod=1.0, max_damage=5, items=None):

        super().__init__(char_name, char_description, constitution, weapon, attack_mod,
                     max_damage, items)

    def pick_char(self, characters, can_cancel=True):

        print("Characters: {0}".format(", ".join([character.name for character in characters])))

        character_dict = {character.name: character for character in characters}

        if can_cancel:
            chosen_character = ""
            while chosen_character != "cancel" and chosen_character not in character_dict.keys():
                chosen_character = input("Choose a character, or type cancel: ")

            if chosen_character == 'cancel':
                return None

        else:
            chosen_character = ""
            while chosen_character not in character_dict.keys():
                chosen_character = input("Choose a character: ")

        return character_dict[chosen_character]

    def pick_item(self, header, item_type=None):

        if item_type is None:
            items_list = [item.name for item in self.items]

        else:
            items_list = [item.name for item in self.items if item.type == item_type ]

        print("\n{0} {1}\n".format(header, ", ".join(items_list)))

        items_dict = {item.name: item for item in self.items}

        item = ""
        while item != "cancel" and item not in items_dict.keys():
            item = input("Enter the item you choose, or type cancel: ")

        if item == "cancel":
            return "cancel"

        return items_dict[item]

    def attack(self, opponents):

        if len(opponents) == 1:
            defender = opponents[0]

        else:
            defender = self.pick_char(opponents, False)

        attack_roll = self.roll_dice() * self.attack_mod
        damage_roll = self.roll_dice(1, self.max_damage)

        return (defender, attack_roll, damage_roll, self.weapon)

    def flee_check(self):

        valid_responses = ['yes', 'y', 'no', 'n']
        response = ''

        while response not in valid_responses:
            response = input("You have {0} hitpoints left. Attempt to flee?"
                             .format(self.constitution)).lower()

        if response == 'yes' or response == 'y':
            return True

        else:
            return False

    def give_item(self):

        item = self.pick_item("Items in you inventory: ")

        if item == 'cancel':
            return None

        self.items.remove(item)
        return item

    def inspect_item(self):

        item = self.pick_item("Here are the item that you may inspect: ")

        if item == 'cancel':
            return None

        return item
