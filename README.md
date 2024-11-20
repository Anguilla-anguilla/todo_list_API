# Todo list API (Django Rest Framework)

This project is a simple Todo API built using Django Rest Framework (DRF). It allows users to manage their todos, including creating, updating, and deleting. The API also includes user authentication using JWT tokens.

## Features

- User registration and login with JWT authentication.
- CRUD operations for todos.
- Pagination and filtering for todo lists.
- Rate limiting and throttling for API requests.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Anguilla-anguilla/todo_list_API.git
   cd your-repo
   ```

2. **Set up a virtual environment**:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- **POST** `/api/token/` - Obtain JWT tokens (access and refresh) by providing valid credentials.
- **POST** `/api/token/refresh/` - Refresh the access token using the refresh token.

### User

- **POST** `/api/auth/users/` - Register a new user.

### Todo

- **GET** `/api/list/` - List all todos for the authenticated user (supports pagination and filtering by `mark_done`).
- **POST** `/api/` - Create a new todo.
- **GET** `/api/{todo_id}` - Retrieve a specific todo.
- **PUT** `/api/{todo_id}` - Update a specific todo (supports partial updates).
- **DELETE** `/api/{todo_id}` - Delete a specific todo.


## Usage Examples

### Create a New Todo

```bash
curl -X POST http://127.0.0.1:8000/api/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your_access_token_here" \
-d '{
    "title": "New Todo",
    "description": "New Description"
}'
```

[Project URL](https://roadmap.sh/projects/todo-list-api)
