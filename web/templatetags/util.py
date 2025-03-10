from django import template
from django.utils.translation import gettext

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

product_name = {
    'pin_header': 'Pin Header',
    'female_header': 'Female Header',
    'box_header': 'Box Header',
    'ejector_header': 'Ejector Header',
    'socket': 'RJ45',
    'jumper': 'Pin Header Jumper',
    'fc': 'IDC Connector & Cable',
    'round_header': 'Machined Pin Header',
    'round_female_header': 'Machined Female Header',
    'ic_socket': 'IC Socket',
    'din': 'Din41612',
    'plcc': 'PLCC',
    'edge': 'EDGE Card Connector',
}

title_code = {
    'zh-hans':'title',
    'en':'en_title',
    'es':'es_title',
    'de':'de_title',
    'fr':'fr_title',
    'ja':'ja_title',
    'ko':'ko_title',
    'ru':'ru_title',
}

@register.filter
def get_name(product, code):
    code = name_code[code]
    return getattr(product, code)


@register.filter
def get_description(product, code):
    code = description_code[code]
    return getattr(product, code)

@register.filter
def get_general_name(input):
    p_name = product_name[input]
    return gettext(p_name)

@register.filter
def get_news_title(news, code):
    code = title_code[code]
    return getattr(news, code)