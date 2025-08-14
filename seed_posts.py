from django.contrib.auth import get_user_model
from blog.models import Post
from django.utils import timezone

User = get_user_model()

# Get admin user
admin_user = User.objects.filter(is_superuser=True).first()
if not admin_user:
    raise Exception(
        "No admin user found! Please create one before running this script."
    )

# Default blog post data
posts_data = [
    {
        "title": "Getting Started with Django",
        "slug": "getting-started-with-django",
        "content": """# Getting Started with Django

Django is a high-level Python web framework that encourages rapid development.

## Steps to Start
1. Install Python
2. Install Django via `pip install django`
3. Run `django-admin startproject myproject`

```bash
django-admin startproject myproject
```

**Tip:** Keep your Django version updated for the latest features and security patches.
""",
        "tags": ["django", "python", "webdev"],
    },
    {
        "title": "Understanding Django ORM",
        "slug": "understanding-django-orm",
        "content": """# Understanding Django ORM

The **Object-Relational Mapper (ORM)** in Django allows you to interact with the database using Python code.

## Example Query
```python
from myapp.models import Post
Post.objects.filter(status='published')
```

ORM abstracts SQL queries, making database interaction safer and more intuitive.
""",
        "tags": ["django", "orm", "database"],
    },
    {
        "title": "Django Model Best Practices",
        "slug": "django-model-best-practices",
        "content": """# Django Model Best Practices

Models are the single source of truth for your database schema.

### Tips:
- Use `verbose_name` for better admin readability.
- Keep models small and focused.
- Use indexes for frequently queried fields.

```python
class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
```
""",
        "tags": ["django", "models", "best-practices"],
    },
    {
        "title": "Working with Django Forms",
        "slug": "working-with-django-forms",
        "content": """# Working with Django Forms

Django provides a powerful forms API for rendering and validating user input.

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
```

Forms handle:
- Validation
- Rendering HTML inputs
- Cleaning data
""",
        "tags": ["django", "forms", "validation"],
    },
    {
        "title": "Django Templates with Markdown",
        "slug": "django-templates-with-markdown",
        "content": """# Django Templates with Markdown

Using Markdown in templates allows for flexible content formatting.

### Example:
```python
import markdown
html = markdown.markdown("# Hello World")
```

You can process Markdown in your templates using a custom filter.
""",
        "tags": ["django", "templates", "markdown"],
    },
    {
        "title": "Django Admin Customization",
        "slug": "django-admin-customization",
        "content": """# Django Admin Customization

The Django admin site is highly customizable.

### Example:
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish')
```

Make the admin interface user-friendly for content managers.
""",
        "tags": ["django", "admin", "customization"],
    },
    {
        "title": "Deploying Django to Production",
        "slug": "deploying-django-to-production",
        "content": """# Deploying Django to Production

Common deployment steps:
1. Use a production server (e.g., Gunicorn, uWSGI)
2. Set `DEBUG = False`
3. Configure static files with `collectstatic`
4. Use a reverse proxy (e.g., Nginx)

```bash
python manage.py collectstatic
```
""",
        "tags": ["django", "deployment", "production"],
    },
    {
        "title": "Django REST Framework Basics",
        "slug": "django-rest-framework-basics",
        "content": """# Django REST Framework Basics

DRF is a powerful toolkit for building APIs in Django.

```python
from rest_framework import serializers
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
```
""",
        "tags": ["django", "rest-api", "drf"],
    },
    {
        "title": "Working with Django Signals",
        "slug": "working-with-django-signals",
        "content": """# Working with Django Signals

Signals allow decoupled applications to get notified when actions occur.

### Example:
```python
from django.db.models.signals import post_save
```
""",
        "tags": ["django", "signals", "architecture"],
    },
    {
        "title": "Django Caching Strategies",
        "slug": "django-caching-strategies",
        "content": """# Django Caching Strategies

Improve performance by caching views, templates, or querysets.

```python
from django.views.decorators.cache import cache_page
@cache_page(60 * 15)
def my_view(request):
    ...
```
""",
        "tags": ["django", "caching", "performance"],
    },
    {
        "title": "Django Authentication System",
        "slug": "django-authentication-system",
        "content": """# Django Authentication System

Django comes with a built-in authentication system for users and permissions.

### Example:
```python
from django.contrib.auth import authenticate
user = authenticate(username='admin', password='secret')
```
""",
        "tags": ["django", "auth", "security"],
    },
    {
        "title": "Django Middleware Explained",
        "slug": "django-middleware-explained",
        "content": """# Django Middleware Explained

Middleware is a framework for globally altering input or output.

### Example:
```python
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
```
""",
        "tags": ["django", "middleware", "request-response"],
    },
    {
        "title": "Using Django with Celery",
        "slug": "using-django-with-celery",
        "content": """# Using Django with Celery

Celery is a distributed task queue that integrates well with Django.

```python
from celery import shared_task
@shared_task
def add(x, y):
    return x + y
```
""",
        "tags": ["django", "celery", "async"],
    },
    {
        "title": "Advanced Django QuerySets",
        "slug": "advanced-django-querysets",
        "content": """# Advanced Django QuerySets

QuerySets can be chained, filtered, and optimized.

```python
Post.objects.filter(status='published').order_by('-publish')[:5]
```
""",
        "tags": ["django", "orm", "queries"],
    },
    {
        "title": "Django Testing with Pytest",
        "slug": "django-testing-with-pytest",
        "content": """# Django Testing with Pytest

Pytest is a fast and simple testing framework that works great with Django.

```bash
pytest
```

### Benefits:
- Cleaner test syntax
- Powerful fixtures
- Faster test runs
""",
        "tags": ["django", "testing", "pytest"],
    },
]

# Create posts
created_posts = []
for post_data in posts_data:
    post, created = Post.objects.get_or_create(
        slug=post_data["slug"],
        defaults={
            "title": post_data["title"],
            "content": post_data["content"],
            "status": "PB",  # Published
            "publish": timezone.now(),
            "author": admin_user,
        },
    )
    if created:
        post.tags.add(*post_data["tags"])
        created_posts.append(post)

print(
    f"✅ Created {len(created_posts)} default blog posts for '{admin_user.username}'."
)
