from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *
from .models import *

class AllListView(ListView):
    queryset = DNS_Shop.objects.all()
    template_name = 'main.html'

class DetailListView(DetailView):
    model = DNS_Shop
    template_name = 'detail.html'

class CreateListView(CreateView):
    model = DNS_Shop
    template_name = 'create_book.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('main')

class UpdateListView(UpdateView):
    model = DNS_Shop
    template_name = 'update_book.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('main')

class DeleteListView(DeleteView):
    queryset = DNS_Shop.objects.all()
    template_name = 'book_confirm.html'

    def get_success_url(self):
        return reverse('main')



