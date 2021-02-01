from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class WordpressApphook(CMSApp):
    app_name = 'wordpress_api'
    name = 'Wordpress'

    def get_urls(self, page=None, language=None, **kwargs):
        return ['wordpress_api.urls']
