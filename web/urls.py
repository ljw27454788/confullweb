from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from web import views
from web import ajax

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    re_path(r'^connectors$', views.ProductListView.as_view(), name='products'),
    re_path(r'^pin-header/(?P<slug>[-\w]+)$', views.PinheaderDetailView.as_view(), name='pin_header_detail'),
    re_path(r'^pin-header$', views.PinheaderListView.as_view(), name='pin_header'),
    re_path(r'^female-header/(?P<slug>[-\w]+)$', views.FemaleheaderDetailView.as_view(), name='female_header_detail'),
    re_path(r'^female-header$', views.FemaleheaderListView.as_view(), name='female_header'),
    re_path(r'^box-header/(?P<slug>[-\w]+)$', views.BoxheaderDetailView.as_view(), name='box_header_detail'),
    re_path(r'^box-header$', views.BoxheaderListView.as_view(), name='box_header'),
    re_path(r'^ejector-header/(?P<slug>[-\w]+)$', views.EjectorheaderDetailView.as_view(), name='ejector_header_detail'),
    re_path(r'^ejector-header$', views.EjectorheaderListView.as_view(), name='ejector_header'),
    re_path(r'^machined-round-pin-header/(?P<slug>[-\w]+)$', views.MachinedpinheaderDetailView.as_view(), name='round_header_detail'),
    re_path(r'^machined-round-pin-header$', views.MachinedpinheaderListView.as_view(), name='round_header'),
    re_path(r'^machined-round-female-header/(?P<slug>[-\w]+)$', views.MachinedfemaleheaderDetailView.as_view(), name='round_female_header_detail'),
    re_path(r'^machined-round-female-header$', views.MachinedfemaleheaderListView.as_view(), name='round_female_header'),
    re_path(r'^pin-header-jumper/(?P<slug>[-\w]+)$', views.JumperDetailView.as_view(), name='jumper_detail'),
    re_path(r'^pin-header-jumper$', views.JumperListView.as_view(), name='jumper'),
    re_path(r'^ic-socket/(?P<slug>[-\w]+)$', views.IcsocketDetailView.as_view(), name='ic_socket_detail'),
    re_path(r'^ic-socket$', views.IcsocketListView.as_view(), name='ic_socket'),
    re_path(r'^edge-card-connector/(?P<slug>[-\w]+)$', views.EdgeDetailView.as_view(), name='edge_detail'),
    re_path(r'^edge-card-connector$', views.EdgeListView.as_view(), name='edge'),
    re_path(r'^idc-connector-cable-fc/(?P<slug>[-\w]+)$', views.FcDetailView.as_view(), name='fc_detail'),
    re_path(r'^idc-connector-cable-fc$', views.FcListView.as_view(), name='fc'),

    re_path(r'^product_filter', ajax.ProductFilterForm, name='product_filter'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)