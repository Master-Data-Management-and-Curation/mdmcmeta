import MetadataCreate

class Database:
    __data : dict = {}

    def store(self, obj:MetadataCreate):
        id = next(self.__gen_id())
        self.__data[id] = obj
    
    def __gen_id(self):
        num = 0
        while True:
            yield num
            num += 1
