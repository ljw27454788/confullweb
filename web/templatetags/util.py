from django import template

register = template.Library()

name_code = {
    'zh-hans':'name',
    'en':'en_name',
    'es':'es_name',
    'de':'de_name',
    'fr':'fr_name',
    'ja':'ja_name',
    'ko':'ko_name',
    'ru':'ru_name',
}

description_code = {
    'zh-hans':'description',
    'en':'en_description',
    'es':'es_description',
    'de':'de_description',
    'fr':'fr_description',
    'ja':'ja_description',
    'ko':'ko_description',
    'ru':'ru_description',
}

@register.filter
def get_name(product, code):
    code = name_code[code]
    return getattr(product, code)


@register.filter
def get_description(product, code):
    code = description_code[code]
    return getattr(product, code)