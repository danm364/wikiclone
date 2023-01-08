from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search_entry"),
    path("<str:title>", views.entry, name="page_entry"),
    
]
