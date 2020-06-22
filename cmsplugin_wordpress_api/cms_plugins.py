from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import LatestBlogs, BlogsByAuthor, BlogsByCategory, BlogsByTag

@plugin_pool.register_plugin
class LatestBlogsPlugin(CMSPluginBase):
    module = "Wordpress Blogs"
    model = LatestBlogs
    render_template = "cmsplugin_wordpress_api/latest_blogs.html"

@plugin_pool.register_plugin
class BlogsByAuthorPlugin(CMSPluginBase):
    module = "Wordpress Blogs"
    model = BlogsByAuthor
    render_template = "cmsplugin_wordpress_api/blogs_by_author.html" 

@plugin_pool.register_plugin
class BlogsByCategoryPlugin(CMSPluginBase):
    module = "Wordpress Blogs"
    model = BlogsByCategory
    render_template = "cmsplugin_wordpress_api/blogs_by_category.html" 

@plugin_pool.register_plugin
class BlogsByTagPlugin(CMSPluginBase):
    module = "Wordpress Blogs"
    model = BlogsByTag
    render_template = "cmsplugin_wordpress_api/blogs_by_tag.html" 
