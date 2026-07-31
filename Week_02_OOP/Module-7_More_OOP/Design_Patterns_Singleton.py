# Singleton --> One Single Instance
# If you want a new instance, you will get the old one(already created) instance


class SingleTon:
    __instance = None
    def __init__(self) -> None:
        if SingleTon.__instance is None:
            SingleTon.__instance = self

        else:
            raise Exception("This is Singleton. Already have an instance, use that one by calling get_instance method")


    @staticmethod
    def get_instance():
        if SingleTon.__instance is None:
            SingleTon()
        return SingleTon.__instance

first = SingleTon.get_instance()
second = SingleTon.get_instance()
third = SingleTon.get_instance()
print(first)
print(second)
print(third)

last = SingleTon()
