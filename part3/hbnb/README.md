# HBNB - Part 3: Persistence Layer & Database Integration

## Overview

This is Part 3 of the **HBNB project**, a simplified clone of Airbnb developed as part of the Holberton School curriculum. In this phase, the focus is on implementing a robust persistence layer — replacing in-memory storage with a relational database backend, and managing relationships between entities using object-relational mapping (ORM).

## Key Objectives

- Integrate a SQL-based database (e.g., SQLite or MySQL)
- Define relationships between models using ORM (e.g., SQLAlchemy)
- Separate repository and model logic from the business and API layers
- Ensure persistence of all major entities: `User`, `Place`, `Amenity`, `Review`

## Features

- Full schema design and class-to-table mapping
- Model relationships:
  - One-to-many (e.g. User → Place)
  - Many-to-many (e.g. Place ↔ Amenity)
- CRUD operations managed via repository classes
- Decoupled architecture for scalability and unit testing

## Project Structure

```text
part3/hbnb/
├── app/
│   ├── models/         # SQLAlchemy models and relationships
│   ├── persistence/    # Repositories and session/database management
│   ├── services/       # Business logic layer (optional)
├── config.py           # Database config and environment settings
├── requirements.txt    # Python dependencies
├── run.py              # Application entry point
```

## **Getting Started**

### **Prerequisites**

   Python 3.8+

   SQLAlchemy

   Flask (if using with the API from Part 2)

   SQLite

### **Installation**

   Clone the repository:

```git
git clone <your-repo-url>
cd part3/hbnb
```

   Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

   Install dependencies:

```bash
pip install -r requirements.txt
```

## **Configuration**

Edit config.py to point to your preferred database URI:

SQLALCHEMY_DATABASE_URI = "sqlite:///hbnb.db"

### Database Initialization

Run migrations or manually create the database schema using the models:

python run.py  # or a dedicated setup script

### **Model Overview**

   User: can own multiple places and post reviews.(one-to-many)

   Place: linked to a user, has many amenities and reviews.

   Amenity: reusable across places (many-to-many).

   Review: linked to both users and places.

Authors

Developed by:

   Dorine Lemee

   Ancelin Chevallier

This educational project is part of the curriculum at Holberton School.
