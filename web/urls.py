from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from web import views
from web import ajax

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^products$', views.ProductListView.as_view(), name='products'),
    re_path(r'^products/Pin-Header/(?P<pk>[-\w]+)$', views.PinheaderDetailView.as_view(), name='pin_header_detail'),
    re_path(r'^products/Pin-Header$', views.PinheaderListView.as_view(), name='pin_header'),
    re_path(r'^products/Female-Header/(?P<pk>[-\w]+)$', views.FemaleheaderDetailView.as_view(), name='female_header_detail'),
    re_path(r'^products/Female-Header$', views.FemaleheaderListView.as_view(), name='female_header'),
    re_path(r'^products/Box-Header/(?P<pk>[-\w]+)$', views.BoxheaderDetailView.as_view(), name='box_header_detail'),
    re_path(r'^products/Box-Header$', views.BoxheaderListView.as_view(), name='box_header'),
    re_path(r'^products/Ejector-Header/(?P<pk>[-\w]+)$', views.EjectorheaderDetailView.as_view(), name='ejector_header_detail'),
    re_path(r'^products/Ejector-Header$', views.EjectorheaderListView.as_view(), name='ejector_header'),
    re_path(r'^products/Machined-Round-Pin-Header/(?P<pk>[-\w]+)$', views.MachinedpinheaderDetailView.as_view(), name='round_header_detail'),
    re_path(r'^products/Machined-Round-Pin-Header$', views.MachinedpinheaderListView.as_view(), name='round_header'),
    re_path(r'^products/Machined-Round-Female-Header/(?P<pk>[-\w]+)$', views.MachinedfemaleheaderDetailView.as_view(), name='round_female_header_detail'),
    re_path(r'^products/Machined-Round-Female-Header$', views.MachinedfemaleheaderListView.as_view(), name='round_female_header'),
    re_path(r'^products/Pin-Header-Jumper/(?P<pk>[-\w]+)$', views.JumperDetailView.as_view(), name='jumper_detail'),
    re_path(r'^products/Pin-Header-Jumper$', views.JumperListView.as_view(), name='jumper'),
    re_path(r'^products/IC-Socket/(?P<pk>[-\w]+)$', views.IcsocketDetailView.as_view(), name='ic_socket_detail'),
    re_path(r'^products/IC-Socket$', views.IcsocketListView.as_view(), name='ic_socket'),
    re_path(r'^products/EDGE-Card-Connector/(?P<pk>[-\w]+)$', views.EdgeDetailView.as_view(), name='edge_detail'),
    re_path(r'^products/EDGE-Card-Connector$', views.EdgeListView.as_view(), name='edge'),

    re_path(r'^product_filter', ajax.ProductFilterForm, name='product_filter'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)