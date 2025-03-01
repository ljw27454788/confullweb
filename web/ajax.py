from django.shortcuts import render
from web.models import Product

def ProductFilterForm(request):
    product_type = request.GET.get('product_type', 'all')
    pitch = request.GET.get('pitch', 'all')
    row = request.GET.get('row', 'all')
    shape = request.GET.get('shape', 'all')
    language_code = request.GET.get('language_code', 'en')
    # print(product_type, pitch, row, shape, language_code)
    if product_type != 'all':
        product = Product.objects.filter(product_type=product_type)
    if pitch != "all":
        product = product.filter(pitch=pitch)
    if row != "all":
        product = product.filter(row__contains=row)
    if shape != "all":
        product = product.filter(shape=shape)

    # if queryset is empty
    if not product:
        return render(request, 'products_filter_message.html', context={
            'LANGUAGE_CODE': language_code,
        })
    return render(request, 'products_list.html', context={
        'object_list': product,
        'LANGUAGE_CODE': language_code,
    })