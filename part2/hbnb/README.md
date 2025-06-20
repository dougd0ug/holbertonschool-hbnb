# HBNB

## Overview

HBNB is a simplified clone of the Airbnb platform, designed as a learning project to demonstrate full-stack web development, RESTful API design, and object-oriented programming in Python. The project is structured to separate concerns between models, services, persistence, and API layers.

## Features

- User registration and profile management
- Place listing with price, location, and description
- Amenity management and association with places
- User reviews and ratings for places
- RESTful API endpoints for all major resources

## Project Structure

```text
part2/hbnb/
├── app/
│   ├── api/           # API namespaces and routes
│   ├── models/        # Data models (User, Place, Amenity, Review)
│   ├── persistence/   # Repository and data storage logic
│   ├── services/      # Business logic and facade
├── config.py          # Configuration settings
├── requirements.txt   # Python dependencies
├── run.py             # Application entry point
├── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- Flask==3.1.1
- flask-restx==1.3.0
- (Recommended) [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd part2/hbnb
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv mon_env
   source mon_env/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
python run.py
```

The API will be available at `http://localhost:5000/`.

### Running Tests

```bash
python -m app.api.v1.test
```

## API Endpoints

- `POST /api/v1/users/` — Create a new user
- `GET /api/v1/users/` — List all users
- `GET /api/v1/users/<user_id>` — Get a specific user
- `PUT /api/v1/users/<user_id>` — Update a user
- `DELETE /api/v1/users/<user_id>` — Delete a user

Similar endpoints exist for places, amenities, and reviews.


## Conclusion

This project is for educational purposes.
It has been made by Dorine Lemee et Ancelin Chevallier

---

*Project by Holberton School students.*
