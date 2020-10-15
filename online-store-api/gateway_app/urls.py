from django.conf.urls import url
from gateway_app import views

urlpatterns = [
    # url(r'^$', views.ItemsList.as_view()),
    # url(r'^(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/$',
    #     views.ItemDetail.as_view()),
    url(r'^$', views.OrdersList.as_view()),
    url(r'^(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/$',
        views.OrderDetail.as_view()),
]