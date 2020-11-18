
class Provider:
    @classmethod
    def get_text(cls):
        return "Hello World!"

    @classmethod
    def calc(cls, data):
        return int(data) + 1