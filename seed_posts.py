from django.contrib.auth import get_user_model
from blog.models import Post
from django.utils import timezone
import random

User = get_user_model()

# Get admin user
admin_user = User.objects.filter(is_superuser=True).first()
if not admin_user:
    raise Exception(
        "No admin user found! Please create one before running this script."
    )

# Sample titles and contents
titles = [
    "Django Tips and Tricks",
    "How to Build a Blog in Django",
    "Understanding Django ORM",
    "Advanced QuerySets in Django",
    "Deploying Django Apps to Production",
    "Custom Managers in Django",
    "Optimizing Django Performance",
    "Using Signals Effectively",
    "Django and Celery Integration",
    "Django REST Framework Essentials",
]

contents = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Proin sed nulla vel justo aliquam tincidunt.",
    "Suspendisse potenti. Etiam varius ligula id augue lacinia, sed sodales odio faucibus.",
    "Fusce luctus risus sed eros fermentum, in bibendum ipsum dignissim.",
    "Donec non dui vel ipsum ullamcorper dapibus.",
    "Vivamus accumsan lectus vitae feugiat mattis.",
    "Curabitur at purus a nunc vehicula posuere.",
    "Nam at risus sit amet magna dignissim convallis.",
    "Phasellus tincidunt augue vitae magna suscipit aliquet.",
    "In hac habitasse platea dictumst.",
]

# Sample tags
tags_list = [
    "django",
    "python",
    "webdev",
    "orm",
    "tips",
    "performance",
    "deployment",
    "signals",
    "celery",
    "rest-api",
]

# Create posts
created_posts = []
for i in range(20):
    title = random.choice(titles)
    slug = title.lower().replace(" ", "-") + f"-{i}"
    content = random.choice(contents) * random.randint(2, 5)
    status = random.choice(["DF", "PB"])
    publish_date = timezone.now() - timezone.timedelta(days=random.randint(0, 30))

    post = Post.objects.create(
        title=title,
        slug=slug,
        content=content,
        status=status,
        publish=publish_date,
        author=admin_user,
    )

    # Assign 2–4 random tags
    selected_tags = random.sample(tags_list, k=random.randint(2, 4))
    post.tags.add(*selected_tags)

    created_posts.append(post)

print(
    f"✅ Created {len(created_posts)} posts for admin user '{admin_user.username}' with tags."
)
