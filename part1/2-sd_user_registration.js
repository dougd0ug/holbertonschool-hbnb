sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call Request User Registration
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Save User Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Save Response
API-->>User: Return User Registration Success/Failure
