from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("register", views.register, name="register"),
    path("add_space", views.add_space, name="add_space"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("edit/<int:id>", views.edit_listing, name="edit_listing"),
    path("search", views.search, name="search"),
    path("searchresults", views.search_results, name="search_results"),
    path("messages/<int:user_id>", views.messages, name="messages"),
]