

'''
Work in progres.....do not run.
'''

class Director():
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_pokemon(self):
        pkmn = Pokemon()

class Pokemon():

    def __init__(self):
        self.__head = None
        self.__body = None
        self.__tail = None
        self.__props = None
