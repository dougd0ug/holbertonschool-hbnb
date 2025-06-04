# **1. Introduction**
## **Purpose of the Document**
This document is a technical presentation of diagrams for our project Hbnb. It brings architecture of the project, design decisions and interactions between all layers and classes.

## **Overview of the project**

**Hbnb** project is a simplified version of Airbnb with some utilities :
- Register as an user and update profile
- Looking for some places with prices, location and description
- Rating places and leave comments about it
- Add some amenities associate to places

# **2. High-Level Architecture**

In this high-level architecture diagram, we want to light on the interactions between the 3 layers :
- **Presentation Layer**: This includes the services and API through which users interact with the system.
- **Business Logic Layer**: This contains the models and the core logic of the application.
- **Persistence Layer**: This is responsible for storing and retrieving data from the database.

## **High-level package diagram**

![diagramme](highleveldiagram.svg)
