```mermaid
flowchart TD

    A[User sends message] --> B[Flask receives POST /api/reply]
    B --> C[GameSession.process_message(message)]

    C --> D[MessageAnalyzer.analyze(message)]
    D --> E{Mood?}

    E -->|rage| F[CalmnessEngine.apply(-35)]
    E -->|calm| G[CalmnessEngine.apply(+10)]
    E -->|neutral| H[CalmnessEngine.apply(-5)]

    F --> I[Update calmness]
    G --> I
    H --> I

    I --> J{Calmness == 0?}

    J -->|Yes| K[Reply: "this is fine..."]
    J -->|No| L[Mauricio.get_reply(mood)]

    K --> M[Return JSON to user]
    L --> M
