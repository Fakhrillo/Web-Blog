# Django Blog Project

A simple blog application built with **Django**, designed as a starting point for future enhancements. This is **Version 1**, currently using **SQLite** for the database.

In future updates, more features and improvements will be added.

---

## Features

* Basic blog setup with Django
* Environment variables managed with `.env`
* `.env.sample` provided for easy configuration
* Uses **SQLite** by default for quick setup
* Project dependency management with **uv**

---

## Prerequisites

* Python 3.10+
* [uv](https://github.com/astral-sh/uv) package manager
* Git (optional, for cloning)

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```

### 2. Create a virtual environment using uv

```bash
uv venv
```

### 3. Activate the virtual environment

* **Linux/MacOS**

```bash
source .venv/bin/activate
```

* **Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 5. Set up environment variables

Copy the provided `.env.sample` to `.env` and adjust values as needed:

```bash
cp .env.sample .env
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

### 8. Run the development server

```bash
python manage.py runserver
```

Your blog should now be running at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

* Visit `/admin` to log in as the superuser and manage blog posts.
* Visit the home page to view the list of posts.
* Add, edit, or delete blog posts through the Django admin interface.

---

## Notes

* **Current Version:** 1.0
* **Database:** SQLite (will be replaced or made configurable in future versions)
* This README will be updated as new features are added.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
