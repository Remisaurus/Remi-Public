# cards/urls.py

from django.urls import path
# Removed: from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card_list"
    ),
]