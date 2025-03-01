from django.shortcuts import render
from django.views import generic

from web.models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html', context={})

# Products List
class ProductListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "products.html"
    context_object_name = 'product_list'

    def get_queryset(self):
        if 'product_type' in self.request.GET:
            product_type = self.request.GET['product_type']
            keyword = ''
            if 'keyword' in self.request.GET:
                keyword = self.request.GET['keyword']
            if product_type == 'all':
                products = Product.objects.filter(Q(name__contains=keyword) | Q(en_name__contains=keyword))
            else:
                products = Product.objects.filter(
                    Q(product_type=product_type) & (Q(name__contains=keyword) | Q(en_name__contains=keyword)))
            return products
        else:
            return Product.objects.order_by('?').all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context

#Pin Header
class PinheaderListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "Pin-Header.html"
    context_object_name = 'pin_header'

    def get_queryset(self):
        return Product.objects.filter(product_type="pin_header")

    def get_context_data(self, *args, **kwargs):
        context = super(PinheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#pin header detail
class PinheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products_detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(PinheaderDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(PinheaderDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#Female Header
class FemaleheaderListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "Female-Header.html"
    context_object_name = 'female_header'

    def get_queryset(self):
        return Product.objects.filter(product_type="female_header")

    def get_context_data(self, *args, **kwargs):
        context = super(FemaleheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#female header detail
class FemaleheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products_detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(FemaleheaderDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(FemaleheaderDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#Box Header
class BoxheaderListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "Box-Header.html"
    context_object_name = 'box_header'

    def get_queryset(self):
        return Product.objects.filter(product_type="box_header")

    def get_context_data(self, *args, **kwargs):
        context = super(BoxheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#box header detail
class BoxheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products_detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(BoxheaderDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(BoxheaderDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#Ejector Header
class EjectorheaderListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "Ejector-Header.html"
    context_object_name = 'ejector_header'

    def get_queryset(self):
        return Product.objects.filter(product_type="ejector_header")

    def get_context_data(self, *args, **kwargs):
        context = super(EjectorheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#box header detail
class EjectorheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products_detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(EjectorheaderDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(EjectorheaderDetailView, self).get_context_data(*args, **kwargs)
        return context