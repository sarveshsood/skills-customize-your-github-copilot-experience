# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build RESTful APIs using the FastAPI framework in Python, focusing on routing, request handling, data models, asynchronous operations, dependency injection, and automatic API documentation generation.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project

#### Description
Install FastAPI and create a basic application structure to get started with building APIs.

#### Requirements
Completed program should:

- Install fastapi and uvicorn packages
- Create a main.py file with a basic FastAPI app instance
- Add a root endpoint that returns a welcome message
- Run the development server and verify it works

### 🛠️ Create Basic API Endpoints

#### Description
Implement GET and POST endpoints for managing a simple resource, such as a list of items.

#### Requirements
Completed program should:

- Create a GET endpoint at /items that returns a list of items
- Create a POST endpoint at /items that accepts new items
- Use Pydantic models for request/response validation
- Store items in memory (list or dictionary)

### 🛠️ Add Advanced Features

#### Description
Enhance the API with path parameters, query parameters, and proper error handling.

#### Requirements
Completed program should:

- Implement GET /items/{item_id} to retrieve a specific item
- Add query parameters for filtering or pagination
- Handle 404 errors when items are not found
- Include proper HTTP status codes and response models

### 🛠️ Implement Advanced FastAPI Features

#### Description
Incorporate advanced FastAPI features including asynchronous endpoints, dependency injection, and API documentation.

#### Requirements
Completed program should:

- Create asynchronous endpoint functions using async/await
- Implement dependency injection for reusable code (e.g., database connections)
- Add request validation and custom response models
- Generate and customize automatic API documentation
- Handle authentication basics (optional advanced feature)