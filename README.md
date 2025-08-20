# College Rank Management and Analytics System

This repository contains a minimal skeleton for a college rank management and analytics system. The frontend is built with Next.js and the backend uses Flask. The project uses **pnpm** as the Node.js package manager.

## Folders

- `frontend/` – Next.js application
- `backend/` – Flask API

## Quick Start

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

The backend will start on `http://127.0.0.1:5000`.

### Frontend

```bash
cd frontend
pnpm install
pnpm run dev
```

The frontend will run on `http://localhost:3000`.

Basic placeholder pages and API endpoints are included for the Admin, Student, Rank Analytics and Report modules. You can extend these according to project requirements.

## User Guide

1. Start the backend and frontend using the steps above.
2. Visit `http://localhost:3000` in your browser to see the welcome page.
3. Use the buttons on the welcome page to navigate to the different modules:
   - **Admin Module** – `/admin`
   - **Student Module** – `/student`
   - **Rank Analytics Module** – `/rank-analytics`
   - **Report Module** – `/report`
4. Each page calls its corresponding API endpoint and displays the returned data.

## Database Setup (MySQL)

The backend uses **Flask-SQLAlchemy** so you can connect it to a MySQL
database. Update the connection string in `backend/app.py` with your database
credentials:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://user:pass@localhost/college"
```

Replace `user` and `pass` with the MySQL username and password that have
access to the `college` database. These credentials are only for the database
connection and are separate from the sample student login.

To sign in to the Student module using the included demo data, enter the
username **`alice`** and password **`password`** in the login form.

SQLAlchemy models are defined in `backend/models.py`. Run `flask shell` and
execute `db.create_all()` to create tables once your MySQL server is running.

Keep database-related code under the `backend/` directory; there is no need to
place MySQL code in the repository root.

## Database Guide

Running `python app.py` in the `backend` folder will create a SQLite database
named `college.db` if it does not exist. On first run, the application
automatically inserts a set of default departments and courses. For details on
inspecting the database or using the SQLite command-line interface, see
[`docs/database-guide.md`](docs/database-guide.md).
