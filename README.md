# Community Service Management System (backend)

A Flask-based system to manage community events, volunteers, tasks, attendance, and reports.

## Features

- **User Management**: Register users with roles.
- **Event Management**: Create events and notify volunteers.
- **Volunteer Management**: Register volunteers and track their hours.
- **Task Assignment**: Assign tasks to events and volunteers.
- **Attendance Tracking**: Log attendance for events.
- **Reports**: Generate reports for volunteer hours.
- **Categories**: Organize and view event categories.

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Authentication**: JWT
- **Password Encryption**: Bcrypt
- **Email Notifications**: Flask-Mail

## Setup

1. **Clone the repo**:
    ```bash
    git clone <repository_url>
    cd community-service-management
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Database**:
    Update `config.py` with your MySQL database URI and email credentials.

4. **Initialize Database**:
    ```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    ```

5. **Run the app**:
    ```bash
    flask run
    ```

## API Endpoints

- **POST /users** - Create a user
- **POST /events** - Create an event (sends notifications)
- **POST /volunteers** - Register a volunteer
- **POST /tasks** - Create a task
- **POST /attendance** - Log attendance

For more details, see the code and comments.

## License

MIT License
