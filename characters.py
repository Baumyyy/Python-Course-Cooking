class Character:
    def get_reply(self, mood):
        raise NotImplementedError("Subclass must implement this method")

class Mauricio(Character):
    def __init__(self, responses):
        self.responses = responses

    def get_reply(self, mood):
        return self.responses[mood]
