from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from django.utils import timezone
from django.conf import settings
from blog.managers import PublishedManager
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


class Post(TimeStampedModel, StatusModel):
    STATUS = [("DF", "Draft"), ("PB", "Published")]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date="publish")
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )

    tags = TaggableManager()
    objects = models.Manager()  # Default manager
    published = PublishedManager()

    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]
        indexes = [models.Index(fields=["created"])]

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
