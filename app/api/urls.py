from django.urls import path
from api import views

urlpatterns = [
    path('<int:cols>/<int:rows>/<str:args>', views.RankView.as_view())
]