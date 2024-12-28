from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *
from .models import *

class AllListView(ListView):
    queryset = Book.objects.all()
    template_name = 'main.html'

class DetailListView(DetailView):
    model = Book
    template_name = 'detail.html'

class CreateListView(CreateView):
    model = Book
    template_name = 'create_book.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('main')

class UpdateListView(UpdateView):
    model = Book
    template_name = 'update_book.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('main')

class DeleteListView(DeleteView):
    queryset = Book.objects.all()
    template_name = 'book_confirm.html'

    def get_success_url(self):
        return reverse('main')



