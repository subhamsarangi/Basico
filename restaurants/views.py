from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm
from django.shortcuts import render, get_object_or_404

class RestaurantListView(ListView):
    def get_queryset(self):
        slug=self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
            Q(category__iexact=slug) |
            Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class=RestaurantLocationCreateForm
    login_url="/login/"
    template_name='restaurants/form.html'
    #success_url='/restaurants/list'
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)
