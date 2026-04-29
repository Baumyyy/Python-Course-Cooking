```mermaid
classDiagram
    class Character {
        +get_reply(mood)
    }

    class Mauricio {
        -responses: dict
        +get_reply(mood)
    }

    class MessageAnalyzer {
        -calm_patterns
        -rage_patterns
        +analyze(message)
    }

    class CalmnessEngine {
        -calmness: int
        +apply(mood)
        +is_game_over()
    }

    class GameSession {
        -analyzer: MessageAnalyzer
        -engine: CalmnessEngine
        -character: Mauricio
        -history: list
        +process_message(message)
    }

    Character <|-- Mauricio
    GameSession --> MessageAnalyzer
    GameSession --> CalmnessEngine
    GameSession --> Mauricio
