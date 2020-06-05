from django import template
from django.http import Http404
                                                                             
from ..utils import WPApiConnector


register = template.Library()                   


@register.simple_tag
def blogs_by_author(slug, number_of_posts):

    connector = WPApiConnector(lang='en', blog_per_page=number_of_posts)

    authors = connector.authors
    if slug in authors:
        wp_filter = {'author': authors[slug]['id']}
    else:
        raise Http404

    blogs = connector.get_posts(wp_filter=wp_filter)

    return blogs['body']
