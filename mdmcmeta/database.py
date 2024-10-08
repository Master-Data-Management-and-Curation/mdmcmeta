from schema import MetadataCreate

class Database:
    __data : dict = {}
    __id_generator : int

    def __init__(self):
        self.__id_generator = self.__gen_id()

    def store(self, obj:MetadataCreate):
        id = next(self.__id_generator)
        self.__data[id] = obj
    
    def __gen_id(self):
        num = 0
        while True:
            yield num
            num += 1
