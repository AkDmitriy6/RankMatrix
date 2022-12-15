from django.urls import path
from rankapp import views

urlpatterns = [
    path("rank", views.main),
]