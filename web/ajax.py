from django.shortcuts import render

def ProductFilterForm(request):
    product_type = request.GET['product_type']
    pitch = request.GET['pitch']
    row = request.GET['row']
    plastic = request.GET['plastic']
    shape = request.GET['shape']
    language_code = request.GET['language_code']
    # product = Product.objects.filter(product_type=product_type)
    # if pitch != "all":
    #     product = product.filter(pitch=pitch)
    # if row != "all":
    #     product = product.filter(row__contains=row)
    # if plastic != "all":
    #     product = product.filter(pnum=plastic)
    # if shape != "all":
    #     if shape == "180" or shape == "90":
    #         product = product.filter(Q(shape=shape) | Q(shape__contains=shape))
    #     else:
    #         product = product.filter(shape=shape)
    # if 'pheight' in request.GET:
    #     pheight = request.GET['pheight']
    #     # other_pheight = request.GET['other_pheight']
    #     if pheight != "all":
    #         product = product.filter(pheight=pheight)
    # if 'molex' in request.GET:
    #     molex = request.GET['molex']
    #     if molex != "all":
    #         if molex == "0":
    #             product = product.exclude(en_name__contains='Molex')
    #         else:
    #             product = product.filter(en_name__contains='Molex')

    # if queryset is empty
    if not product:
        return render(request, 'product/product_message.html', context={
            'LANGUAGE_CODE': language_code,
        })
    return render(request, 'product/product_detail_list.html', context={
        'object_list': product,
        'LANGUAGE_CODE': language_code,
    })