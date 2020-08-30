# from dataclasses import dataclass

class Item():

    def __init__(self, item_name, item_type, item_description=None):

        self._name = item_name
        self._description = item_description
        self._item_type = item_type


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, item_name):
        self._name = item_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, item_description):
        self._description = item_description

    @property
    def type(self):
        return self._item_type

    @type.setter
    def type(self, item_type):
        self._item_type = item_type

    def __str__(self):

        if self.type == 'story':
            return "{0} ({1}\n\n{2}".format(self.name, self.type, self.description)

        return "{0} ({1}): {2}".format(self.name, self.type, self.description)