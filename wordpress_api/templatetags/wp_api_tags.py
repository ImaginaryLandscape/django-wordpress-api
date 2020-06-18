import iso8601
from django import template
from django.http import Http404
from django.conf import settings                                                                             
from django.core.cache import cache

from ..utils import WPApiConnector


register = template.Library()                   

try:
    cache_time = settings.WP_API_BLOG_CACHE_TIMEOUT
except AttributeError:
    cache_time = 0

@register.simple_tag
def blogs_by_author(slug, number_of_posts):

    connector = WPApiConnector(lang='en', blog_per_page=number_of_posts)

    authors = connector.authors
    if slug in authors:
        wp_filter = {'author': authors[slug]['id']}
    else:
        return

    blogs = cache.get("blog_author_more_context_" + slug)
    blogs = connector.get_posts(wp_filter=wp_filter) if blogs is None else blogs
    cache.add("blog_author_more_context_" + slug, blogs, cache_time)


    # The below code, copied from the views, is needed to add additional data to the context objects.
    # Should we split it out into a common function somehow to avoid repeating?
    tags = connector.tags
    categories = connector.categories

    for blog in blogs['body']:
        blog_categories = []
        if 'categories' in blog:
            for category in categories:
                if category['id'] in blog['categories']:
                    blog_categories.append(category)
        blog['category_list'] = blog_categories
        blog_tags = []
        if 'tags' in blog:
            for tag in tags:
                if tag['id'] in blog['tags']:
                    blog_tags.append(tag)
        blog['tag_list'] = blog_tags
        blog['slug'] = str(blog['slug'])
        blog['bdate'] = iso8601.parse_date(blog['date']).date()
        featured_media = blog.get(
            '_embedded', {}).get('wp:featuredmedia', [])
        authors = blog.get(
            '_embedded', {}).get('author', [])
        if featured_media:
            blog['featured_image'] = featured_media[0]
        if authors:
            blog['authors'] = authors

    return blogs['body']
