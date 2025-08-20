# Database Guide

This project uses SQLite by default. When you run `python app.py` inside the
`backend` directory, Flask-SQLAlchemy creates a file named `college.db` in the
same directory. Tables are created automatically and the application seeds
initial department and course data.

## Inspecting the Database via Command Line

1. Change to the backend directory:

   ```bash
   cd backend
   ```

2. Launch the interactive Flask shell:

   ```bash
   flask shell
   ```

3. Inside the shell, you can query models using SQLAlchemy:

   ```python
   from models import Department, Course
   Department.query.all()
   ```

If you prefer the raw SQLite command line, use:

```bash
sqlite3 college.db
```

From there you can run standard SQL commands like `SELECT * FROM department;`.
