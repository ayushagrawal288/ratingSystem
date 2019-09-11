from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(), name='list'),
    url(r'^products/(?P<id>\d+)/$', views.RatingGet.as_view(), name='rating')
]