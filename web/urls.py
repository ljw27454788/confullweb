from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from web import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^products$', views.ProductListView.as_view(), name='products'),
    re_path(r'^products/Pin-Header/(?P<pk>[-\w]+)$', views.PinHeaderDetailView.as_view(), name='pin_header_detail'),
    re_path(r'^products/Pin-Header', views.PinheaderListView.as_view(), name='pin_header'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)