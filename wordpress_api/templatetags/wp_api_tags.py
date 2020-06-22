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

def add_blog_context(connector, blogs):
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
    return blogs

@register.simple_tag
def latest_blogs(number_of_posts):
    connector = WPApiConnector(lang='en', blog_per_page=number_of_posts)

    blogs = cache.get("blog_latest_blogs_context_count_" + str(number_of_posts))
    blogs = connector.get_posts() if blogs is None else blogs
    cache.add("blog_latest_blogs_context__count_" + str(number_of_posts), blogs, cache_time)

    blogs = add_blog_context(connector, blogs)

    return blogs['body']

@register.simple_tag
def blogs_by_author(slug, number_of_posts):
    connector = WPApiConnector(lang='en', blog_per_page=number_of_posts)

    authors = connector.authors
    if slug in authors:
        wp_filter = {'author': authors[slug]['id']}
    else:
        return

    blogs = cache.get("blog_author_tag_context_" + slug + '_count_' + str(number_of_posts))
    blogs = connector.get_posts(wp_filter=wp_filter) if blogs is None else blogs
    cache.add("blog_author_tag_context_" + slug + '_count_' + str(number_of_posts), blogs, cache_time)

    blogs = add_blog_context(connector, blogs)

    return blogs['body']


@register.simple_tag
def blogs_by_category(slug, number_of_posts):
    connector = WPApiConnector(lang='en', blog_per_page=number_of_posts)

    categories = connector.categories
    category = None
    for c in categories:
        if c['slug'] == slug:
            category = c
            break
    if category is not None:
        wp_filter = {'categories': category['id']}
    else:
        return

    blogs = cache.get("blog_categories_tag_context_" + slug + '_count_' + str(number_of_posts))
    blogs = connector.get_posts(wp_filter=wp_filter) if blogs is None else blogs
    cache.add("blog_categories_tag_context_" + slug + '_count_' + str(number_of_posts), blogs, cache_time)

    blogs = add_blog_context(connector, blogs)

    return blogs['body']

@register.simple_tag
def blogs_by_tag(slug, number_of_posts):
    connector = WPApiConnector(lang='en', blog_per_page=number_of_posts)

    tags = connector.tags
    tag = None
    for t in tags:
        if t['slug'] == slug:
            tag = t
            break
    if tag is not None:
        wp_filter = {'tags': tag['id']}
    else:
        return

    blogs = cache.get("blog_tags_tag_context_" + slug + '_count_' + str(number_of_posts))
    blogs = connector.get_posts(wp_filter=wp_filter) if blogs is None else blogs
    cache.add("blog_tags_tag_context_" + slug + '_count_' + str(number_of_posts), blogs, cache_time)

    blogs = add_blog_context(connector, blogs)

    return blogs['body']
