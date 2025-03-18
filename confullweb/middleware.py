from django.utils.deprecation import MiddlewareMixin
# from django.http import HttpResponseNotAllowed
from confullweb import settings

class BlockSearchEngineRedirectMiddleware(MiddlewareMixin):
    """
    阻止搜索引擎爬虫的自动语言重定向
    """
    SEARCH_ENGINE_USER_AGENTS = [
        'Googlebot', 'Bingbot', 'Slurp', 'DuckDuckBot', 'Baiduspider',
        'YandexBot', 'Sogou', 'Exabot', 'facebot', 'ia_archiver'
    ]

    def process_request(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        is_search_engine = any(ua in user_agent for ua in self.SEARCH_ENGINE_USER_AGENTS)
        
        if is_search_engine:
            # 强制禁用语言重定向
            request.session['django_language'] = settings.LANGUAGE_CODE  # 设为默认语言
            request.LANGUAGE_CODE = settings.LANGUAGE_CODE