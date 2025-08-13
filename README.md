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
git clone https://github.com/Fakhrillo/Web-Blog.git
cd Web-Blog
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Set up environment variables

Copy the provided `.env.sample` to `.env` and adjust values as needed:

```bash
cp .env.sample .env
```

### 4. Apply database migrations

```bash
uv run manage.py migrate
```

### 5. Create a superuser (admin)

```bash
uv run manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

### 6. Run the development server

```bash
uv run manage.py runserver
```

Your blog should now be running at: [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)

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
