sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call (Request Places using filters)
API->>BusinessLogic: Fetch corresponding Places
BusinessLogic->>Database: Request corresponding places Data
Database-->>BusinessLogic: Return Place Data
BusinessLogic-->>API: Return Places List
API-->>User: Places List Sent
