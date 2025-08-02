# Flask API Template

A well-structured and feature-rich template for building RESTful APIs using Flask. This template provides a solid foundation with user authentication, database integration, and a clean project structure to kickstart your next project.

## Features

*   **Scalable Project Structure:** Organized into modules like `controllers`, `models`, `services`, and `configs` for better maintainability.
*   **User Authentication:** Comes with ready-to-use email/password login and user profile management.
*   **OAuth Integration:** Includes a pre-configured module for Google OAuth 2.0.
*   **Database Ready:** Integrated with Flask-SQLAlchemy for database operations and Flask-Migrate for handling database schema migrations.
*   **Configuration Management:** A flexible configuration system that separates settings for different environments.
*   **Middleware Support:** Custom middleware for handling database sessions.
*   **Command-Line Interface:** Includes `commands.py` for custom management scripts.

## Project Structure

The repository is organized as follows to ensure a clean and scalable architecture:

```
📦 flask-api-template
├─ .gitattributes
├─ .gitignore
├─ AUTHORS
├─ app.py
├─ commands.py
├─ configs
│  ├─ __init__.py
│  ├─ app_config.py
│  ├─ deploy
│  │  └─ __init__.py
│  ├─ feature
│  │  ├─ __init__.py
│  │  └─ security.py
│  ├─ middleware
│  │  ├─ __init__.py
│  │  └─ database.py
│  └─ oauth
│     ├─ __init__.py
│     └─ google.py
├─ controllers
│  ├─ console
│  │  ├─ __init__.py
│  │  ├─ auth
│  │  │  └─ login.py
│  │  ├─ user
│  │  │  └─ profile.py
│  │  └─ wraps.py
│  └─ ui
│     ├─ __init__.py
│     └─ page
│        └─ content.py
├─ extensions
│  ├─ ext_database.py
│  ├─ ext_login.py
│  └─ ext_migrate.py
├─ fields
│  └─ profile_field.py
├─ libs
│  ├─ external_api.py
│  ├─ helper.py
│  ├─ login.py
│  └─ passport.py
├─ models
│  ├─ __init__.py
│  └─ user.py
├─ requirements.txt
└─ services
   └─ account_service.py
```

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)
*   A virtual environment tool (`venv` or `virtualenv`)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/nquangit/flask-api-template.git
    cd flask-api-template
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    This project likely uses environment variables for configuration. Create a `.env` file in the root directory and add the necessary configuration keys. Refer to the `configs/app_config.py` file to see what is required.

    Example `.env` file:
    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    SQLALCHEMY_DATABASE_URI_SCHEME="sqlite"
    DATABASE_URI="db.sqlite3"
    SECRET_KEY="your-super-secret-key"

    # Google OAuth Credentials
    GOOGLE_CLIENT_ID="your-google-client-id"
    GOOGLE_CLIENT_SECRET="your-google-client-secret"
    ```

5.  **Set up the database:**
    Initialize the database and run the migrations to create the necessary tables.
    ```sh
    flask db init # or flask init-db  # Run only once to initialize migrations
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

### Running the Application

Once the setup is complete, you can start the development server:

```sh
flask run
```

The application will be available at `http://127.0.0.1:5000`.

## Usage

The template provides several API endpoints out of the box.

*   **Authentication:**
    *   `POST /api/auth/login`: Log in a user.
    *   `GET /api/auth/logout`: Log out a user.
*   **User Profile:**
    *   `GET /api/user/profile`: Get the profile of the currently logged-in user.

The API endpoints are defined in the `controllers/console` directory. The UI pages are handled by the `controllers/ui` directory.

## Core Dependencies

This project relies on several key Python libraries:

*   **Flask:** The core web framework.
*   **Flask-SQLAlchemy:** For database ORM integration.
*   **Flask-Migrate:** For handling database migrations with Alembic.
*   **Flask-Login:** For managing user sessions and authentication.
*   **Flask-WTF:** For handling forms and CSRF protection.

For a complete list, please see the `requirements.txt` file.

## Contributing

Contributions are welcome! If you have suggestions for improvement or want to add new features, please feel free to create a pull request or open an issue.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---
