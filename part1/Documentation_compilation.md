# **Documentation compilation**

## **1. Introduction**

### **Purpose of the Document**

This section is a technical presentation of diagrams for our project Hbnb. It brings architecture of the project, design decisions and interactions between all layers and classes.

### **Overview of the project**

**Hbnb** project is a simplified version of Airbnb with some utilities :

- Register as an user and update profile
- Looking for some places with prices, location and description
- Rating places and leave comments about it
- Add some amenities associate to places

## **2. High-Level Architecture**

In this high-level architecture diagram, we want to light on the interactions between the 3 layers :

- **Presentation Layer**: This includes the services and API through which users interact with the system.
- **Business Logic Layer**: This contains the models and the core logic of the application.
- **Persistence Layer**: This is responsible for storing and retrieving data from the database.

### **High-level package diagram**

![highleveldiagram.svg](https://www.mermaidchart.com/app/projects/4f606910-aade-4225-97bf-a75f73d348bc/diagrams/39abef38-27ca-4c3e-848c-8e29b1a4f96b/version/v0.1/edit)

## **3. Business Logic Layer**

This section is a presentation of different classes and entities of the project. Every entities have attributes and methods, with relations between them, for the logic of the project.

### **Entities**

#### **1. User Entity**

- Attributes
  - `id: UUID`
  - `first_name: string`
  - `last_name: string`
  - `email: string`
  - `password: String`
  - `admin: Boolean`
  - `created_at: date`
  - `updated_at: date`
- Methods
  - `register_user() : void`
  - `update_user() : void`
  - `delete_user() : void`

#### **2. Place Entity**

- Attributes
  - `id: UUID`
  - `title: string`
  - `description: string`
  - `price: float`
  - `latitude: float`
  - `longitude: float`
- Methods
  - `create_place() : void`
  - `update_place() : void`
  - `delete_place() : void`
  - `list_place() : void`

#### **3. Review Entity**

- Attributes
  - `id: UUID`
  - `user: string`
  - `place: string`
  - `rating: int`
  - `comment: string`
- Methods
  - `create_review() : void`
  - `update_review() : void`
  - `delete_review() : void`
  - `list_review() : void`

#### **4. Amenity Entity**

- Attributes
  - `id: UUID`
  - `name: string`
  - `description: string`
- Methods
  - `create_amenity() : void`
  - `update_amenity() : void`
  - `delete_amenity() : void`
  - `list_amenity() : void`

### **Detailed Class Diagram for Business Logic Layer**

lien

## **4. Sequence Diagrams**

![User Creation Sequence Diagram](https://1drv.ms/i/c/38d5dae183484409/EXhuoazAsmtFtCgseqoYxZEBs009yR5azT2WspJTfoMHOg?e=RdcDkq)
