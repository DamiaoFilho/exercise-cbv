from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from .models import Reserve
from .forms import ReserveForm
# Create your views here.

class ReserveCreateView(CreateView):
    model = Reserve
    form_class = ReserveForm
    template_name = "hotel/create.html"
    success_url = "/hotel/list/"

class ReserveListView(ListView):
    model = Reserve
    template_name = "hotel/list.html"

class ReserveUpdateView(UpdateView):
    model = Reserve
    form_class = ReserveForm
    template_name = "hotel/create.html"
    success_url = "/hotel/list/"

class ReserveDeleteView(DeleteView):
    model = Reserve
    success_url = "/hotel/list/"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.delete(self.get_object())

        return redirect("list")