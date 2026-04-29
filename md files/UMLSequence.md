```mermaid
sequenceDiagram
    participant User
    participant FlaskApp
    participant GameSession
    participant Analyzer as MessageAnalyzer
    participant Engine as CalmnessEngine
    participant Mauricio

    User->>FlaskApp: POST /api/reply (message)
    FlaskApp->>GameSession: process_message(message)

    GameSession->>Analyzer: analyze(message)
    Analyzer-->>GameSession: mood

    GameSession->>Engine: apply(mood)
    Engine-->>GameSession: calm_change

    GameSession->>Mauricio: get_reply(mood)
    Mauricio-->>GameSession: reply_text

    GameSession-->>FlaskApp: reply_text, calm_change, calmness
    FlaskApp-->>User: JSON response
