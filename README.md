# ToDo Application using Django Rest Framework (DRF)

This project implements a ToDo application using Django Rest Framework (DRF) that allows users to manage their tasks. It provides endpoints for creating, editing, deleting, marking tasks as complete, scheduling tasks, and receiving reminders for pending tasks.

## Table of Contents

- [API Endpoints](#api-endpoints)
  - [Task Endpoints](#task-endpoints)
  - [User Authentication Endpoints](#user-authentication-endpoints)
- [Project Structure](#project-structure)
- [Running the Project](#running-the-project)
- [Usage](#usage)

## API Endpoints

### Task Endpoints

#### Create Task
- Endpoint: `POST /todo/create-todo/`
- Description: Create a new ToDo task.
- Request Body:
    ```json
    {
        "title": "Task Title",
        "description": "Task Description (Optional)",
        "scheduled_at": "YYYY-MM-DDThh:mm:ssZ"
    }
    ```
- Response: Returns the created task details.

#### List Tasks
- Endpoint: `GET /todo/todo-list/`
- Description: Get a list of all ToDo tasks.
- Response: Returns a list of tasks.

#### Retrieve, Update, Delete Task
- Endpoint: `GET /todo/update-todo/<task_id>/`, `PUT /todo/update-todo/<task_id>/`, `DELETE /todo/delete-todo/<task_id>/`
- Description: Retrieve, update, or delete a specific task identified by `<task_id>`.

#### Mark Task as Complete
- Endpoint: `PUT /todo/<task_id>/complete/`
- Description: Mark a task as complete.
- Response: Returns the updated task details.

#### Schedule/Reschedule Task
- Endpoint: `PUT /todo/<task_id>/reschedule/`
- Description: Reschedule a task by updating its scheduled time.
- Request Body:
    ```json
    {
        "scheduled_at": "YYYY-MM-DDThh:mm:ssZ"
    }
    ```
- Response: Returns the updated task details.


### User Authentication Endpoints

#### Register User
- Endpoint: `POST /users/register/`
- Description: Register a new user.
- Request Body:
    ```json
    {
        "username": "new_user",
        "password": "password123"
    }
    ```
- Response: Returns the created user details.

#### Login User (Get Authentication Token)
- Endpoint: `POST /users/login/`
- Description: Log in an existing user and retrieve an authentication token.
- Request Body:
    ```json
    {
        "username": "existing_user",
        "password": "password123"
    }
    ```
- Response: Returns an authentication token for the logged-in user.

### Custom Search Endpoints

#### Search Tasks by Title
- Endpoint: `GET /todo/searchByTitle/?title=<search_query>`
- Description: Search tasks by title. Performs a case-insensitive search for tasks containing the specified query string in their title.
- Response: Returns a list of tasks matching the search query.

#### Search Tasks by Date Range
- Endpoint: `GET /todo/searchByDate/?start_date=<DD-MM-YYYY>&end_date=<DD-MM-YYYY>`
- Description: Retrieve tasks scheduled within the specified date range.
- Response: Returns a list of tasks scheduled within the given date range.

### Reminder Notifications

The project implements a reminder notification system for pending tasks. Reminders are checked periodically for tasks scheduled within a certain time frame (15 minutes in this implementation) and simulated by printing reminders to the console. For production use, integrate your preferred notification method (e.g., email, SMS) to send reminders to users.

## Project Structure

- `todo/models.py`: Defines the `TodoTask` model for tasks.
- `todo/serializers.py`: Serializers for the `TodoTask` model.
- `todo/views.py`: Views and API endpoints for tasks, search, and reminders.
- `todo/urls.py`: URL patterns for the defined endpoints.
- `todo_project/settings.py`: Django project settings.

## Running the Project

1. Install required packages: `pip install -r requirements.txt`
2. Apply migrations: `python manage.py migrate`
3. Start the development server: `python manage.py runserver`

## Usage

- Use API client tools like Postman or cURL to interact with the implemented endpoints.
- Create, update, delete tasks using the provided endpoints.
- Search for tasks by title or within a specific date range using the respective search endpoints.
