from django.urls import path
from .views import *
urlpatterns = [
    path('', AllListView.as_view(), name='main'),
    path('create', CreateListView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailListView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateListView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteListView.as_view(), name='delete'),

]