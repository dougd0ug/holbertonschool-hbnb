sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call (Review Submission)
API->>BusinessLogic: Validate and Process Submission
BusinessLogic->>Database: Save Review Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Review Registration confirmed
