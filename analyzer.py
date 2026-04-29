import re

class MessageAnalyzer:
    def __init__(self, calm_patterns, rage_patterns):
        self.calm_patterns = calm_patterns
        self.rage_patterns = rage_patterns

    def analyze(self, message):
        if self.rage_patterns.search(message):
            return 'rage'
        if self.calm_patterns.search(message):
            return 'calm'
        return 'neutral'
