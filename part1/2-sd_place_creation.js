sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call (Place creation request)
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Save Place Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Place Registration confirmed
