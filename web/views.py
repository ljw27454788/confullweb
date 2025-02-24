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