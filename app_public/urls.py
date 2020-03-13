from django.urls import path, include, re_path as url
from .views import HomeView

urlpatterns = [

    url(r'^$',
        view=HomeView.as_view(),
        name='index'),

]