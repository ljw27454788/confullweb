from modeltranslation.translator import register, TranslationOptions
from web.models import Product, News

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
        'seo_description',
    )

@register(News)
class BlogTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'content',
        'seo_description',
    )