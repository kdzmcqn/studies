class Room():

    def __init__(self, room_name, description):

        self._name = room_name
        self._description = description
        self._characters = []
        self._item = None
        self._search_gen = None
        self.linked_rooms = {}


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
    def description(self, room_description):
        self._description = room_description

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, characters):
        self._characters = characters

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def search_gen(self):
        return self._search_gen

    @search_gen.setter
    def search_gen(self, search_responses):
        self._search_gen = self.search(search_responses)


    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link


    def move(self, direction, party):

        if direction in self.linked_rooms:
            self.linked_rooms[direction].characters += party
            self.characters = [character for character in self.characters
                               if character not in party]
            return self.linked_rooms[direction]

        else:
            print("\nYou can't go that way.")
            return self


    def search(self, search_responses):
        for response in search_responses:
            yield response

        while True:
            yield ("You find nothing new.", False)


    def __str__(self):

        roomStr = "The {0}\n".format(self.name)
        roomStr += "-" * 20 + "\n"
        roomStr += "{0}\n\n".format(self.description)

        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            roomStr += "The {0} is {1}.\n".format(room.name, direction)

        return roomStr
