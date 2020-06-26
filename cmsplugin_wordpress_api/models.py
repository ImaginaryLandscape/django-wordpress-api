from cms.models.pluginmodel import CMSPlugin
from django.db import models
from .utils import get_authors, get_categories, get_tags

LAYOUT_CHOICES = (
    ('grid', 'Grid'),
    ('list', 'List'),
    ('featured', 'Featured'),
)

class BaseBlogList(CMSPlugin):
    number_to_display = models.IntegerField(default=4,
        help_text="The number of blog posts to be displayed"
    )
    layout = models.CharField(default="grid", choices=LAYOUT_CHOICES, 
        max_length=55)

    class Meta:
        abstract = True

class LatestBlogs(BaseBlogList):
    pass

class BlogsByAuthor(BaseBlogList):
    authors = models.TextField(blank=True)

class BlogsByCategory(BaseBlogList):
    categories = models.TextField(blank=True)

class BlogsByTag(BaseBlogList):
    tags = models.TextField(blank=True)
