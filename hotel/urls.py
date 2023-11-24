from django.urls import path
from .views import *
urlpatterns = [
    path("create/", ReserveCreateView.as_view(), name="create"),
    path("update/<int:pk>", ReserveUpdateView.as_view(), name="update"),
    path("list/", ReserveListView.as_view(), name="list"),
    path("delete/<int:pk>", ReserveDeleteView.as_view(), name="delete")
]



