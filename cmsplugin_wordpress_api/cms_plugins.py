from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django import forms
from .models import LatestBlogs, BlogsByAuthor, BlogsByCategory, BlogsByTag
from .utils import get_authors, get_categories, get_tags


class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['authors'] = forms.ChoiceField(choices=get_authors())

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['categories'] = forms.ChoiceField(choices=get_categories())

class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields['tags'] = forms.ChoiceField(choices=get_tags())

@plugin_pool.register_plugin
class LatestBlogsPlugin(CMSPluginBase):
    module = "Wordpress Blogs"
    model = LatestBlogs
    render_template = "cmsplugin_wordpress_api/latest_blogs.html"

@plugin_pool.register_plugin
class BlogsByAuthorPlugin(CMSPluginBase):
    form = AuthorForm
    module = "Wordpress Blogs"
    model = BlogsByAuthor
    render_template = "cmsplugin_wordpress_api/blogs_by_author.html" 

@plugin_pool.register_plugin
class BlogsByCategoryPlugin(CMSPluginBase):
    form = CategoryForm
    module = "Wordpress Blogs"
    model = BlogsByCategory
    render_template = "cmsplugin_wordpress_api/blogs_by_category.html" 

@plugin_pool.register_plugin
class BlogsByTagPlugin(CMSPluginBase):
    form = TagForm
    module = "Wordpress Blogs"
    model = BlogsByTag
    render_template = "cmsplugin_wordpress_api/blogs_by_tag.html" 
