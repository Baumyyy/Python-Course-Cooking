from analyzer import MessageAnalyzer
from game import CalmnessEngine
from characters import Mauricio

class GameSession:
    def __init__(self, calm_patterns, rage_patterns, responses):
        self.analyzer = MessageAnalyzer(calm_patterns, rage_patterns)
        self.engine = CalmnessEngine()
        self.character = Mauricio(responses)
        self.history = []

    def process_message(self, message):
        mood = self.analyzer.analyze(message)
        change = self.engine.apply(mood)
        reply = self.character.get_reply(mood)
        self.history.append((message, mood, change, reply))
        return reply, change, self.engine.calmness
