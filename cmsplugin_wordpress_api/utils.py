from django.utils.safestring import mark_safe
from wordpress_api.utils import WPApiConnector

def get_authors():
    connector = WPApiConnector(lang='en')
    authors = connector.authors
    choices = []
    for author in authors:
        choices.append((authors[author]["slug"], mark_safe(authors[author]["name"])))

    return choices

def get_categories():
    connector = WPApiConnector(lang='en')
    categories = connector.categories
    choices = []
    for category in categories:
        choices.append((category["slug"], mark_safe(category["name"])))

    return choices

def get_tags():
    connector = WPApiConnector(lang='en')
    tags = connector.tags
    choices = []
    for tag in tags:
        choices.append((tag["slug"], mark_safe(tag["name"])))

    return choices
