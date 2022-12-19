from django.urls import path 
from .views import AOTListView,AOTDetailView,TitanListView,TitanDetailView,AOTCreateView
urlpatterns = [
    path('',AOTCreateView.as_view(),name='AOT_create'),
    path('<int:pk>',AOTDetailView.as_view(),name='AOT_detail'),
    path('Titan/',TitanListView.as_view(),name='Titan_list'),
    path('Titan/<int:pk>',TitanDetailView.as_view(),name='Titan_detail')
]