from django.shortcuts import render
from django.views import generic

from web.models import Product, News

# Create your views here.
def index(request):
    return render(request, 'index.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})

# def company(request):
#     return render(request, 'company.html', context={})

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
    context_object_name = 'pin-header'

    def get_queryset(self):
        return Product.objects.filter(product_type="pin-header")

    def get_context_data(self, *args, **kwargs):
        context = super(PinheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#pin header detail
class PinheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

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
    context_object_name = 'female-header'

    def get_queryset(self):
        return Product.objects.filter(product_type="female-header")

    def get_context_data(self, *args, **kwargs):
        context = super(FemaleheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#female header detail
class FemaleheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

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
    context_object_name = 'box-header'

    def get_queryset(self):
        return Product.objects.filter(product_type="box-header")

    def get_context_data(self, *args, **kwargs):
        context = super(BoxheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#box header detail
class BoxheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

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
    context_object_name = 'ejector-header'

    def get_queryset(self):
        return Product.objects.filter(product_type="ejector-header")

    def get_context_data(self, *args, **kwargs):
        context = super(EjectorheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#ejector header detail
class EjectorheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(EjectorheaderDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(EjectorheaderDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#Machined Pin Header
class MachinedpinheaderListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "Machined-Pin-Header.html"
    context_object_name = 'round-header'

    def get_queryset(self):
        return Product.objects.filter(product_type="round-header")

    def get_context_data(self, *args, **kwargs):
        context = super(MachinedpinheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#Machined Pin detail
class MachinedpinheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(MachinedpinheaderDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(MachinedpinheaderDetailView, self).get_context_data(*args, **kwargs)
        return context


#Machined Female Header
class MachinedfemaleheaderListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "Machined-Female-Header.html"
    context_object_name = 'round-female-header'

    def get_queryset(self):
        return Product.objects.filter(product_type="round-female-header")

    def get_context_data(self, *args, **kwargs):
        context = super(MachinedfemaleheaderListView, self).get_context_data(*args, **kwargs)
        return context
    
#Machined Female detail
class MachinedfemaleheaderDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(MachinedfemaleheaderDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(MachinedfemaleheaderDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#Pin Header Jumper
class JumperListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "Pin-Header-Jumper.html"
    context_object_name = 'jumper'

    def get_queryset(self):
        return Product.objects.filter(product_type="jumper")

    def get_context_data(self, *args, **kwargs):
        context = super(JumperListView, self).get_context_data(*args, **kwargs)
        return context
    
#Jumper detail
class JumperDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(JumperDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(JumperDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#IC Socket
class IcsocketListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "IC-Socket.html"
    context_object_name = 'ic-socket'

    def get_queryset(self):
        return Product.objects.filter(product_type="ic-socket")

    def get_context_data(self, *args, **kwargs):
        context = super(IcsocketListView, self).get_context_data(*args, **kwargs)
        return context
    
#IC Socket detail
class IcsocketDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(IcsocketDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(IcsocketDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#EDGE
class EdgeListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "EDGE-Card-Connector.html"
    context_object_name = 'edge'

    def get_queryset(self):
        return Product.objects.filter(product_type="edge")

    def get_context_data(self, *args, **kwargs):
        context = super(EdgeListView, self).get_context_data(*args, **kwargs)
        return context
    
#EDGE detail
class EdgeDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(EdgeDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(EdgeDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#IDC FC
class FcListView(generic.ListView):
    paginate_by = 8
    model = Product
    template_name = "FC-IDC-Cable.html"
    context_object_name = 'fc'

    def get_queryset(self):
        return Product.objects.filter(product_type="fc")

    def get_context_data(self, *args, **kwargs):
        context = super(FcListView, self).get_context_data(*args, **kwargs)
        return context
    
#IDC FC detail
class FcDetailView(generic.DetailView):
    model = Product
    template_name = "products-detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(FcDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(FcDetailView, self).get_context_data(*args, **kwargs)
        return context
    

#News
class NewsListView(generic.ListView):
    model = News
    template_name = "News.html"
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all().order_by('-created_at')

    def get_context_data(self, *args, **kwargs):
        context = super(NewsListView, self).get_context_data(*args, **kwargs)
        return context
    
#News detail
class NewsDetailView(generic.DetailView):
    model = News
    template_name = "news-detail.html"

    def get_object(self, *args, **kwargs):
        obj = super(NewsDetailView, self).get_object(*args, **kwargs)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(NewsDetailView, self).get_context_data(*args, **kwargs)
        context['product_type'] = self.object.about
        return context