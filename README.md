# Django Blog Project

A modern, responsive **Django Blog** application with a polished UI, **PostgreSQL** database, and full **Docker** support.  
This is **Version 2**, featuring a completely redesigned frontend with **dark mode**, improved search, and a cleaner layout.

---

## ✨ Features

- **Responsive, modern UI** with improved typography, layout, and styling
- **Dark mode** toggle with preference saved in the browser
- **Full-text search** integrated into the main navigation
- **PostgreSQL** as the default database
- **Dockerized setup** for easy deployment
- **Environment-based configuration** with `.env`
- Pagination, tag filtering, and related post suggestions
- Commenting system and share-by-email feature

---

## 🛠 Prerequisites

- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- Git (optional, for cloning)

---

## 🚀 Quick Start with Docker

### 1. Clone the repository

```bash
git clone https://github.com/Fakhrillo/Web-Blog.git
cd Web-Blog
```

### 2. Configure environment variables

Copy the sample configuration and update values if needed:

```bash
cp .env.sample .env
```

By default, `.env.sample` contains settings for PostgreSQL and Django.

### 3. Build and start the services

```bash
docker compose up --build -d
```

This will start:
- **Django app** (with hot reload in development)
- **PostgreSQL database**


### 4. Create an admin user

```bash
docker compose exec web uv run manage.py createsuperuser
```

---

## 📍 Access the App

- Blog: [http://localhost:8000/blog/](http://localhost:8000/blog/)  
- Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 💻 Development Notes

- The app is pre-configured to use PostgreSQL inside Docker.
- You can still run Django locally without Docker by installing dependencies and updating `.env` for your local database.
- Frontend enhancements include:
  - Centered search bar in the header
  - Fully styled pagination buttons
  - Clean post cards with hover effects
  - Dark mode toggle with smooth transitions

---

## 📂 Project Structure

```
Web-Blog/
│── blog/                # Main app with views, models, templates
│── templates/           # HTML templates
│── static/              # CSS, JS, images
│── Dockerfile
│── docker-compose.yml
│── .env
│── .env.sample
│── manage.py
```

---

## 📝 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.
