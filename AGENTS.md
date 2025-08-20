# Guidelines for Codex

This repository contains a minimal starter for a College Rank Management and Analytics System. The project is divided into two main folders:

- `frontend/` – Next.js application.
- `backend/` – Flask API.

## Building and Testing

Whenever you modify JavaScript/TypeScript code under `frontend/`, run the following from the `frontend` directory:

```bash
pnpm install  # installs dependencies
pnpm run build
```

For Python code in `backend/`, check syntax with:

```bash
python -m py_compile app.py
```

Include any output from these commands in the PR testing section.

## Project Structure Notes

The project currently only implements a minimal example page and a single API endpoint. Future modules should expand on this skeleton:

1. **Admin Module** – manage departments, courses and students.
2. **Student Module** – student login and performance view.
3. **Rank Analytics Module** – generate rank lists and trends.
4. **Report Module** – export reports to Excel/PDF.

## PR Summary Guidance

In PR summaries, briefly describe which module or component you changed and reference the file paths of important modifications.
