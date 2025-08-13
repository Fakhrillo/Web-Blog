from django.contrib.sitemaps import Sitemap
from blog.models import Post

class PostSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.published.all()

    # def location(self, item):
    #     return item.get_absolute_url()

    def lastmod(self, obj):
        return obj.modified